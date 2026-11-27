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
    template = template or getTemplate()
    json, MTI, message, length = _parseHeaderAndMti(message, template=template, encoding=encoding)
    version = getVersion(MTI)

    result, message, length = loopMessage(message, length, template[version], encoding=encoding)
    json.update(MTI=MTI, BMP=result.pop("DE000"))
    json.update(result)
    if version == IsoVersion._1993:
        json = buildPdsElement(json=json)
    json["Length"] = length
    return json


def parseMessageType(message, template=None, encoding=None):
    """Reads only the message type indicator (MTI) of a raw ISO 8583 message.

    Unlike parse, it does not read any data element, so it still returns the
    MTI when a later field of the message is malformed.

    Args:
        message (bytes): raw ISO 8583 message.
        template (dict, optional): message template. Defaults to the current template.
        encoding (str, optional): text encoding of the message, e.g. "cp500". Defaults to the current encoding.

    Returns:
        str: the MTI, starting with 0 or 1, e.g. "0100".

    Raises:
        ValueError: if the message is missing, too short to hold an MTI, or does not start with a valid MTI.
    """
    try:
        _, MTI, _, _ = _parseHeaderAndMti(message, template=template or getTemplate(), encoding=encoding)
    except (TypeError, IndexError):
        raise ValueError("Unable to read the MTI of the message")
    getVersion(MTI)
    return MTI


def _parseHeaderAndMti(message, template, encoding):
    headerRule = template[IsoVersion._1987].getHeaderRule()
    message, json = headerRule.parse(data=message, json={})
    MTI, message, length = parseElement(message, elementId="MTI", template=template[IsoVersion._1987], encoding=encoding)
    return json, MTI, message, length


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
