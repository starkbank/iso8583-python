from bisect import bisect_left as bisectLeft, insort
from .mastercard import mastercard
from .utils.binary import Binary
from . import getEncoding
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


def parse(message, template=mastercard, encoding=None):
    MTI, message, length = parseElement(message, elementId="MTI", template=template[IsoVersion._1987], encoding=encoding)
    version = getVersion(MTI)
    result, message, length = loopMessage(message, length, template[version], encoding=encoding)
    json = dict(MTI=MTI, BMP=result.pop("DE000"))
    json.update(result)
    if version == IsoVersion._1993:
        json.update({"PDS": buildPdsElement(json)})
    json["Length"] = length
    return json


def loopMessage(message, length, template, encoding=None):
    result = {}
    indexes = [0]
    for number in indexes:
        id = getElementId(number)
        if isBitmap(id):
            additionalIndexes, message, delta = parseBitmap(message, elementId=id, template=template)
            length += delta
            result.update({id: additionalIndexes})
            indexes.extend(additionalIndexes)
            continue
        value, message, delta = parseElement(message, elementId=id, template=template, encoding=encoding)
        length += delta
        result[id] = value
    return result, message, length


def parseElement(message, elementId, template, encoding=None):
    rule = template[elementId]
    size = rule["limit"]
    if rule["type"]:
        if len(message) < rule["type"]:
            raise ValueError("expected length {expected}, got {got} in message {elementId}: {message}".format(
                expected=rule["type"],
                got=len(message),
                elementId=elementId,
                message=message,
            ))
        parseSize = int(message[:rule["type"]].decode(encoding or getEncoding()) or 0)
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
        message = message[rule["type"]:]
    element, partial = message[:size], message[size:]
    if size != len(element):
        raise ValueError("expected length {expected}, got {got} in element {elementId}: {element}".format(
            expected=size,
            got=len(element),
            elementId=elementId,
            element=element,
        ))
    result = rule["parser"](element, encoding=encoding)
    return result, partial, rule["type"] + size


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


def unparse(parsed, template=mastercard, encoding=None):
    parsed = parsed.copy()
    output = b""
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
    output += unparseElement(parsed, elementId="MTI", template=template[version], encoding=encoding)
    output += unparseBitmap(BMP, elementId="DE000", template=template[version])
    for id in elementIds:
        if isBitmap(id):
            output += unparseBitmap(BMS, elementId=id, template=template[version])
            continue
        output += unparseElement(parsed, elementId=id, template=template[version], encoding=encoding)
    return output


def unparseBitmap(keys, elementId, template):
    indexes = tuple(elementNumber(key) for key in keys)
    binaryString = Binary.fromIndexes(indexes=indexes, offset=64 * int((min(indexes) - 1) // 64))
    rule = template[elementId]
    return rule["unparser"](binaryString)


def unparseElement(json, elementId, template, encoding=None):
    data = json[elementId]
    rule = template[elementId]
    size = rule["limit"]
    unparsed = rule["unparser"](data, encoding=encoding)[:size]
    if rule["type"]:
        return str(len(unparsed)).zfill(rule["type"]).encode(encoding or getEncoding()) + unparsed
    if len(unparsed) != size:
        raise ValueError("{elementId}: Expected length {lenExpected}, got {lenActual}".format(
            elementId=elementId,
            lenExpected=size,
            lenActual=len(unparsed)
        ))
    return unparsed


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
