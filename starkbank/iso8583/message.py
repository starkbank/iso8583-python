from bisect import bisect_left as bisectLeft
from .mastercard import mastercard
from .utils.binary import Binary
from . import getEncoding


def getVersion(MTI):
    versionMap = {
        "0": "1987",
        "1": "1993",
    }
    try:
        return versionMap[MTI[0]]
    except KeyError:
        raise ValueError("Expected '0' or '1' in MTI[0] (Actual: {MTI}), please check iso8583.encoding".format(MTI=MTI))


def parse(message, template=mastercard):
    MTI, message, length = parseElement(message, elementId="MTI", template=template["1987"])
    version = getVersion(MTI)
    result, message, length = loopMessage(message, length, template[version])
    json = dict(MTI=MTI, BMP=result.pop("DE000"))
    json.update(result)
    json["Length"] = length
    return json


def loopMessage(message, length, template):
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
        value, message, delta = parseElement(message, elementId=id, template=template)
        length += delta
        result[id] = value
    return result, message, length


def parseElement(message, elementId, template):
    rule = template[elementId]
    size = rule["limit"]
    if rule["type"]:
        parseSize = int(message[:rule["type"]].decode(getEncoding()) or 0)
        size = min(size, parseSize)
        if parseSize > size:
            raise ValueError(
                "Expected a maximum of {size} characters, got {parseSize} in {elementId} for message {message}".format(
                    size=size,
                    parseSize=parseSize,
                    elementId=elementId,
                    message=message,
                )
            )
        message = message[rule["type"]:]
    result = rule["parser"](message[:size])
    partial = message[size:]
    size = rule["type"] + size
    return result, partial, size


def parseBitmap(message, elementId, template):
    rule = template[elementId]
    size = rule["limit"]
    binary = rule["parser"](message[:size])
    partial = message[size:]
    offset = 64 if elementNumber(elementId) else 0
    result = Binary.toIndexes(binary, offset=offset)
    return result, partial, 8


def unparse(parsed, template=mastercard):
    output = b""
    version = getVersion(parsed["MTI"])
    elementIds = sorted(key for key in set(parsed) if "DE" in key)
    index = bisectLeft(elementIds, "DE065")
    finalIndex = bisectLeft(elementIds, "DE129")
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
    data = json[elementId]
    rule = template[elementId]
    size = rule["limit"]
    unparsed = rule["unparser"](data)[:size]
    if rule["type"]:
        return str(len(unparsed)).zfill(rule["type"]).encode(getEncoding()) + unparsed
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
