from copy import deepcopy
from . import getTemplate
from .version import IsoVersion
from .utils.pds import buildPdsElement, breakPdsElement
from .utils.bitmap import getBitmapFields, isBitmap, getElementId


def getVersion(MTI):
    versionMap = {
        "0": IsoVersion._1987,
        "1": IsoVersion._1993,
    }
    try:
        return versionMap[MTI[0]]
    except KeyError:
        raise ValueError("Expected '0' or '1' in MTI[0] (Actual: {MTI}), please check iso8583.encoding".format(MTI=MTI))


def parse(message, template=None, encoding=None):
    json, template = {}, template or getTemplate()
    headerRule = template[IsoVersion._1987].getHeaderRule()
    message, json = headerRule.parse(data=message, json=json)

    MTI, message, length = parseElement(message, elementId="MTI", template=template[IsoVersion._1987], encoding=encoding)
    version = getVersion(MTI)

    result, message, length = loopMessage(message, length, template[version], encoding=encoding)
    json.update(MTI=MTI, BMP=result.pop("DE000"))
    json.update(result)
    if version == IsoVersion._1993:
        json = buildPdsElement(json=json)
    json["Length"] = length
    return json


def unparse(parsed, template=None, encoding=None):
    template = template or getTemplate()
    parsed = deepcopy(parsed)
    output = b""

    version = getVersion(parsed["MTI"])
    if version == IsoVersion._1993:
        parsed = breakPdsElement(json=parsed)

    parsed.update(getBitmapFields(json=parsed))
    elementIds = sorted(key for key in parsed if "DE" in key)

    output += unparseElement(parsed, elementId="MTI", template=template[version], encoding=encoding)
    for id in elementIds:
        output += unparseElement(parsed, elementId=id, template=template[version], encoding=encoding)

    headerRule = template[IsoVersion._1987].getHeaderRule()
    output = headerRule.unparse(data=output, json=parsed) + output
    return output


def loopMessage(message, length, template, encoding):
    result = {}
    indexes = [0]
    for number in indexes:
        id = getElementId(number)
        value, message, parsedLength = parseElement(message=message, elementId=id, template=template, encoding=encoding)
        length += parsedLength
        result[id] = value
        if isBitmap(id):
            indexes.extend(value)
    return result, message, length


def parseElement(message, elementId, template, encoding):
    field = template.getField(elementId)
    return field.parse(data=message, encoding=encoding)


def unparseElement(parsed, elementId, template, encoding):
    field = template.getField(elementId)
    return field.unparse(value=parsed[elementId], encoding=encoding)
