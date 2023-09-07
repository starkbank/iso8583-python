from bisect import bisect_left as bisectLeft, insort
from starkbank.iso8583.template.mastercard import mastercard
from starkbank.iso8583.utils.binary import Binary
from starkbank.iso8583.utils.enum import Encoding, PaddingDirection, LengthType
from .utils.integer import Integer
from . import getEncoding
from .utils.length import getLengthBytesLength, parseLength, getDataLengthFromDataEncoding, unparseLength
from .utils.parser import parsePds, unparsePds
from .version import IsoVersion


additionalDataElements = "DE048", "DE062", "DE123", "DE124", "DE125"


def getVersion(MTI):
    versionMap = {
        "0": IsoVersion._1987,
        "1": IsoVersion._1993,
    }
    try:
        return versionMap[MTI[0]]
    except KeyError:
        raise ValueError("Expected '0' or '1' in MTI[0] (Actual: {MTI}), please check iso8583.encoding".format(MTI=MTI))


def parse(message, template=mastercard):
    json = {}

    headerRule = template[IsoVersion._1987].get("Header")
    if headerRule:
        headers, message = headerRule["parser"](message)
        json.update(headers)

    MTI, message, length = parseElement(message, elementId="MTI", template=template[IsoVersion._1987])
    version = getVersion(MTI)

    result, message, length = loopMessage(message, length, template[version])
    json.update(MTI=MTI, BMP=result.pop("DE000"))
    json.update(result)
    if version == IsoVersion._1993:
        json.update({"PDS": buildPdsElement(json)})
    json["Length"] = length
    return json


def loopMessage(message, length, template):
    result = {}
    indexes = [0]
    for number in indexes:
        id = getElementId(number)
        if isBitmap(id):
            additionalIndexes, message, parsedLength = parseBitmap(message, elementId=id, template=template)
            length += parsedLength
            result[id] = additionalIndexes
            indexes.extend(additionalIndexes)
            continue
        value, message, parsedLength = parseElement(message, elementId=id, template=template)
        length += parsedLength
        result[id] = value
    return result, message, length


def parseElement(message, elementId, template):
    rule = template[elementId]
    size = rule["limit"]

    lengthBytes = getLengthBytesLength(lengthType=rule["lengthType"], encoding=rule["lengthEncoding"])  # TODO: come up with a better name
    if lengthBytes:
        if len(message) < lengthBytes:
            raise ValueError("expected length {expected}, got {got} in message {elementId}: {message}".format(
                expected=lengthBytes,
                got=len(message),
                elementId=elementId,
                message=message,
            ))
        parseSize = parseLength(lengthData=message[:lengthBytes], lengthEncoding=rule["lengthEncoding"])
        if parseSize > size:
            raise ValueError(
                "Expected a maximum of {size} characters, got {parseSize} in {elementId} for message {message}".format(
                    size=size,
                    parseSize=parseSize,
                    elementId=elementId,
                    message=message,
                )
            )
        size = parseSize
        message = message[lengthBytes:]

    dataLength = getDataLengthFromDataEncoding(parseSize=size, dataEncoding=rule["dataEncoding"])
    element, partial = message[:dataLength], message[dataLength:]
    if dataLength != len(element):
        raise ValueError("expected length {expected}, got {got} in element {elementId}: {element}".format(
            expected=dataLength,
            got=len(element),
            elementId=elementId,
            element=element,
        ))
    result = rule["parser"](element, encoding=rule["dataEncoding"])

    unpadMethod = rule.get("unpad")
    if unpadMethod:
        result = unpadMethod(element=result, length=size)

    return result, partial, lengthBytes + dataLength


def parseBitmap(message, elementId, template):
    rule = template[elementId]
    size = rule["limit"]
    bytemap, partial = message[:size], message[size:]
    binary = rule["parser"](bytemap)
    offset = 64 if elementNumber(elementId) else 0
    if len(bytemap) != 8:
        raise ValueError("expected length {expected}, got {got} in bitmap {elementId}: {bytemap}".format(
            expected=8,
            got=len(bytemap),
            elementId=elementId,
            bytemap=bytemap,
        ))
    result = Binary.toIndexes(binary, offset=offset)
    return result, partial, 8


def unparse(parsed, template=mastercard):
    parsed = parsed.copy()
    output = b""

    headerRule = template[IsoVersion._1987].get("Header")
    if headerRule:
        output += headerRule["unparser"](parsed)

    version = getVersion(parsed["MTI"])
    if version == IsoVersion._1993:
        parsed.update(breakPdsElement(parsed["PDS"]))

    elementIds = sorted(key for key in set(parsed) if "DE" in key)
    index = bisectLeft(elementIds, "DE065")
    finalIndex = bisectLeft(elementIds, "DE129")

    if finalIndex > index and "DE001" not in elementIds:
        insort(elementIds, "DE001")
        index += 1
        finalIndex += 1

    BMP = elementIds[:index]
    BMS = elementIds[index:finalIndex]

    output += unparseElement(parsed, elementId="MTI", template=template[version])
    output += unparseBitmap(BMP, elementId="DE000", template=template[version])
    for id in elementIds:
        if isBitmap(id):
            output += unparseBitmap(BMS, elementId=id, template=template[version])
            continue
        output += unparseElement(parsed, elementId=id, template=template[version])
    return output


def unparseBitmap(keys, elementId, template):
    indexes = tuple(elementNumber(key) for key in keys)
    binaryString = Binary.fromIndexes(indexes=indexes, offset=64 * int((min(indexes) - 1) // 64))
    rule = template[elementId]
    return rule["unparser"](binaryString)


def unparseElement(json, elementId, template):
    element = json[elementId]
    rule = template[elementId]

    lengthBytes = getDataLengthFromDataEncoding(parseSize=rule["limit"], dataEncoding=rule["dataEncoding"])

    padMethod = rule.get("pad")
    paddedLength = 0
    if padMethod:
        element, paddedLength = padMethod(element)

    data = rule["unparser"](element, encoding=rule["dataEncoding"])[:lengthBytes]

    elementLength = generateElementLength(
        data=data,
        element=element,
        paddedLength=paddedLength,
        lengthType=rule["lengthType"],
        dataEncoding=rule["dataEncoding"],
    )
    lengthData = unparseLength(length=elementLength, lengthType=rule["lengthType"], lengthEncoding=rule["lengthEncoding"])

    if not lengthData and len(data) != lengthBytes:
        raise ValueError("{elementId}: Expected length {lenExpected}, got {lenActual}".format(
            elementId=elementId,
            lenExpected=lengthBytes,
            lenActual=len(data)
        ))
    return lengthData + data


def generateElementLength(data, element, paddedLength, lengthType, dataEncoding):
    length = 0
    if lengthType == LengthType.fixed:
        return length

    if dataEncoding in [Encoding.cp500, Encoding.ascii]:
        length = len(data)
    if dataEncoding == Encoding.binary:
        length = len(data)
    if dataEncoding == Encoding.bcd:
        length = len(element)

    return length - paddedLength


def getBitmap(json):
    return sorted([elementNumber(key) for key in json.keys() if key.startswith("DE")])


def isBitmap(elementId):
    number = elementNumber(elementId)
    return (number % 64) == 1 or number == 0


def elementNumber(elementId):
    return int(elementId.replace("DE", "").strip())


def getElementId(number):
    return "DE" + str(number).zfill(3)


def buildPdsElement(json):
    PDS = {}
    for de in additionalDataElements:
        PDS.update(parsePds(json.get(de, "")))
    return PDS


def breakPdsElement(PDS):
    PDS = PDS.copy()
    json = {}
    pdsElements = iter(additionalDataElements)
    while PDS:
        json[next(pdsElements)] = unparsePds(PDS)
    return json
