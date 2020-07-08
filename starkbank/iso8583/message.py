from bisect import bisect_left

from starkbank.iso8583.templates import mastercard
from starkbank.iso8583.utils.binary import Binary


def parse(message, template=mastercard):
    message, MTI = parseElement(message, elementId="MTI", template=template)
    message, result = loopMessage(message, template)
    return dict(result, MTI=MTI, BMP=result.pop("DE000"))


def loopMessage(message, template):
    result = {}
    indexes = [0]
    for number in indexes:
        id = getElementId(number)
        if isBitmap(id):
            message, additionalIndexes = parseBitmap(message, elementId=id, template=template)
            result.update({id: additionalIndexes})
            indexes.extend(additionalIndexes)
            continue
        message, value = parseElement(message, elementId=id, template=template)
        result[id] = value
    return message, result


def parseElement(message, elementId, template):
    rule = template[elementId]
    size = rule["limit"]
    if rule["type"]:
        size = min(rule["limit"], int(message[:rule["type"]] or 0))
        message = message[rule["type"]:]
    result = rule["parser"](message[:size])
    partial = message[size:]
    return partial, result


def parseBitmap(message, elementId, template):
    rule = template[elementId]
    size = rule["limit"]
    binary = Binary.fromHex(message[:size])
    partial = message[size:]
    offset = 64 if elementNumber(elementId) else 0
    result = Binary.toIndexes(binary, offset=offset)
    return partial, result


def unparse(parsed, template=mastercard):
    output = ""
    elementIds = sorted(key for key in set(parsed) if "DE" in key)
    index = bisect_left(elementIds, "DE065")
    finalIndex = bisect_left(elementIds, "DE129")
    BMP = elementIds[:index]
    BMS = elementIds[index:finalIndex]
    output += unparseElement(parsed, "MTI", template)
    output += unparseBitmap(BMP)
    for id in elementIds:
        if isBitmap(id):
            output += unparseBitmap(BMS)
            continue
        output += unparseElement(parsed, id, template=template)
    return output


def unparseBitmap(keys):
    indexes = tuple(elementNumber(key) for key in keys)
    binaryString = Binary.fromIndexes(indexes=indexes, offset=64 * int((min(indexes) - 1) // 64))
    hexString = Binary.toHex(binaryString)
    return hexString.upper()


def unparseElement(message, elementId, template):
    data = message[elementId]
    if data:
        info = template.get(elementId)
        lengthType = info["type"]
        var = str(len(data)).zfill(lengthType) if lengthType else ""
        return var + data
    return ""


def isBitmap(elementId):
    number = elementNumber(elementId)
    return (number % 64) == 1 or number == 0


def elementNumber(elementId):
    return int(elementId.replace("DE", "").strip())


def getElementId(number):
    return "DE" + str(number).zfill(3)