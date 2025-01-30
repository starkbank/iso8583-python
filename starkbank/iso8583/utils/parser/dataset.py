from copy import deepcopy
from ..binary import Binary


class ParseDataset:

    def parse(self, data, **_kwargs):
        json = {}
        while data:
            datasetId, datasetContent, data = _processDataset(data)
            json.setdefault(datasetId, []).append(datasetContent)
        return json

    def unparse(self, value, **_kwargs):
        value = deepcopy(value)
        data = b"".join(
            _unparseDataset(datasetId=id, content=dataset)
            for id, datasets in sorted(value.items())
            for dataset in datasets
        )
        return data, len(data)

    def byteLength(self, length):
        return length


def _processDataset(data):
    datasetId, data = _parseDatasetId(data=data)
    datasetLength, data = _parseDatasetLength(data=data)
    fieldData, data = data[:datasetLength], data[datasetLength:]
    content = _parseDatasetContent(data=fieldData)
    return datasetId, content, data


def _unparseDataset(datasetId, content):
    idData = _unparseDatasetId(datasetId)
    contentData = _unparseDatasetContent(content)
    lengthData = _unparseDatasetLength(len(contentData))
    return idData + lengthData + contentData


def _parseDatasetId(data):
    idData, data = data[:1], data[1:]
    return Binary.toHex(idData), data


def _unparseDatasetId(datasetId):
    return Binary.fromHex(datasetId)


def _parseDatasetLength(data):
    lengthData, data = data[:2], data[2:]
    return Binary.toInteger(lengthData), data


def _unparseDatasetLength(length):
    return Binary.fromInteger(number=length, byteLength=2)


def _parseDatasetContent(data):
    json = {}
    while data:
        tag, data = _parseTag(data)
        length, data = _parseLength(data)
        valueData, data = data[:length], data[length:]
        json[tag] = _parseValue(valueData)
    return json


def _unparseDatasetContent(content):
    data = b""
    for tag, value in sorted(content.items()):
        tagData = _unparseTag(tag)
        valueData = _unparseValue(value)
        lengthData = _unparseLength(len(valueData))
        data += tagData + lengthData + valueData
    return data


def _parseTag(data):
    tagData, data = data[:1], data[1:]
    tagBits = Binary.toBitString(tagData)
    isNextByteTag = tagBits[-5:] == "11111"
    if isNextByteTag:
        tagData += data[:1]
        data = data[1:]

    tag = Binary.toHex(tagData)
    return tag, data


def _unparseTag(tag):
    return Binary.fromHex(tag)


def _parseLength(data):
    lengthData, data = data[:1], data[1:]
    lengthBits = Binary.toBitString(lengthData)
    isLengthExtended = lengthBits[0] == "1"
    if isLengthExtended:
        byteLength = Binary.toInteger(Binary.fromBitString(lengthBits[1:]))
        lengthData, data = data[:byteLength], data[byteLength:]
    return Binary.toInteger(lengthData), data


def _unparseLength(length):
    if length < 128:
        return Binary.fromInteger(length, byteLength=1)

    lengthData = Binary.fromInteger(length)
    lengthHeaderData = Binary.fromBitString("1" + Binary.toBitString(Binary.fromInteger(len(lengthData)))[1:])
    return lengthHeaderData + lengthData


def _parseValue(data):
    return Binary.toHex(data)


def _unparseValue(value):
    return Binary.fromHex(value)
