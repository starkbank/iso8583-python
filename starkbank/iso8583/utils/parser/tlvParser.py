from enum import Enum
from ... import getEncoding


class TlvElementConfig(Enum):

    DE108 = {
        "subElementKey":    2,
        "subElementLength": 3,
        "subFieldKey":    2,
        "subFieldLength": 2,
    }

    DE112 = {
        "subElementKey":    3,
        "subElementLength": 3,
        "subFieldKey":    None,
        "subFieldLength": None,
    }


class TlvParser:

    _encoding = None
    _dataElement = None

    def __init__(self, encoding=None, dataElement=None):
        self._encoding = encoding
        self._dataElement = dataElement

    def parse(self, data, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        config = self._dataElement.value
        return _parseElements(
            data=data,
            keyLength=config["subElementKey"],
            lengthSize=config["subElementLength"],
            encoding=encoding,
            prefix="SE",
            subKeyLength=config["subFieldKey"],
            subLengthSize=config["subFieldLength"],
        )

    def unparse(self, value, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        config = self._dataElement.value
        data = _unparseElements(
            json=value,
            keyLength=config["subElementKey"],
            lengthSize=config["subElementLength"],
            encoding=encoding,
            prefix="SE",
            subKeyLength=config["subFieldKey"],
            subLengthSize=config["subFieldLength"],
        )
        return data, self._logicalLength(data)

    def byteLength(self, length):
        return length

    def encoding(self):
        return self._encoding or getEncoding()

    @staticmethod
    def _logicalLength(value):
        return len(value)

def _parseElements(data, keyLength, lengthSize, encoding, prefix, subKeyLength=None, subLengthSize=None):
    result = {}
    while data:
        key = data[0:keyLength].decode(encoding)
        length = int(data[keyLength:keyLength + lengthSize].decode(encoding))
        value = data[keyLength + lengthSize:keyLength + lengthSize + length]
        data = data[keyLength + lengthSize + length:]
        if subKeyLength is not None:
            result[prefix + key.zfill(keyLength)] = _parseElements(
                data=value,
                keyLength=subKeyLength,
                lengthSize=subLengthSize,
                encoding=encoding,
                prefix="SF",
            )
            continue
        result[prefix + key.zfill(keyLength)] = value.decode(encoding)
    return result
                                                                                                                                                                                   
def _unparseElements(json, keyLength, lengthSize, encoding, prefix, subKeyLength=None, subLengthSize=None):
    data = b""
    for key, value in sorted(json.items()):
        key = key.replace(prefix, "").zfill(keyLength)
        if subKeyLength is not None:
            valueData = _unparseElements(
                json=value,
                keyLength=subKeyLength,
                lengthSize=subLengthSize,
                encoding=encoding,
                prefix="SF",
            )
            data += key.encode(encoding) + str(len(valueData)).zfill(lengthSize).encode(encoding) + valueData
            continue
        valueData = value.encode(encoding)
        data += key.encode(encoding) + str(len(valueData)).zfill(lengthSize).encode(encoding) + valueData
    return data
                   
