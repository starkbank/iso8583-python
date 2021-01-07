from bisect import bisect_left as bisectLeft
from .mastercard import mastercard
from .utils.binary import Binary


def parse(message, template=mastercard):
    message, MTI = parseElement(message, elementId="MTI", template=template)
    message, result = loopMessage(message, template)
    json = dict(MTI=MTI, BMP=result.pop("DE000"))
    json.update(result)
    return json


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
    binary = rule["parser"](message[:size])
    partial = message[size:]
    offset = 64 if elementNumber(elementId) else 0
    result = Binary.toIndexes(binary, offset=offset)
    return partial, result


def unparse(parsed, template=mastercard):
    output = ""
    elementIds = sorted(key for key in set(parsed) if "DE" in key)
    index = bisectLeft(elementIds, "DE065")
    finalIndex = bisectLeft(elementIds, "DE129")
    BMP = elementIds[:index]
    BMS = elementIds[index:finalIndex]
    output += unparseElement(parsed, elementId="MTI", template=template)
    output += unparseBitmap(BMP, elementId="DE000", template=template)
    for id in elementIds:
        if isBitmap(id):
            output += unparseBitmap(BMS, elementId=id, template=template)
            continue
        output += unparseElement(parsed, elementId=id, template=template)
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
        return str(len(unparsed)).zfill(rule["type"]) + unparsed
    if len(unparsed) != size:
        raise ValueError("{elementId}: Expected length {lenExpected}, got {lenActual}".format(
            elementId=elementId,
            lenExpected=size,
            lenActual=len(unparsed)
        ))
    return unparsed


def isBitmap(elementId):
    number = elementNumber(elementId)
    return (number % 64) == 1 or number == 0


def elementNumber(elementId):
    return int(elementId.replace("DE", "").strip())


def getElementId(number):
    return "DE" + str(number).zfill(3)
