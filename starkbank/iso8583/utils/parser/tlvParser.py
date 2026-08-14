from enum import Enum
from ... import getEncoding


class TlvElementConfig(Enum):

    DE108 = {
        "subElementKey":    2,
        "subElementLength": 3,
        "subFieldKey":    2,
        "subFieldLength": 2,
        # composite subelements per DMAS spec (Tables 1142-1145); plain-value ones
        # must stay raw strings: SE06 (QR Dynamic Code Data), SE12/SE13 (Receiver/Sender
        # Organization Name, GLB 11737.2, ans...140, no subfields) and any unknown
        "compositeSubElements": ("01", "02", "03", "04", "05", "07", "08", "09", "10", "11"),
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
            compositeKeys=config.get("compositeSubElements"),
        )

    def unparse(self, value, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        # jsons produced before TLV parsing hold the whole element as a string
        if isinstance(value, str):
            data = value.encode(encoding)
            return data, self._logicalLength(data)
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

def _parseElements(data, keyLength, lengthSize, encoding, prefix, subKeyLength=None, subLengthSize=None, compositeKeys=None):
    result = {}
    while data:
        key = data[0:keyLength].decode(encoding)
        length = int(data[keyLength:keyLength + lengthSize].decode(encoding))
        value = data[keyLength + lengthSize:keyLength + lengthSize + length]
        data = data[keyLength + lengthSize + length:]
        if subKeyLength is not None and (compositeKeys is None or key in compositeKeys):
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
        # plain-value subelements parse to strings, composite ones to dicts;
        # deciding by type keeps parse/unparse round-trips lossless
        if subKeyLength is not None and isinstance(value, dict):
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
                   
