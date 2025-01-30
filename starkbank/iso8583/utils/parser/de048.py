from copy import deepcopy
from ... import getEncoding


class ParseDe048:

    _encoding = None

    def __init__(self, encoding=None):
        self._encoding = encoding

    def parse(self, data, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        json = {
            "SE00": data[0:1].decode(encoding)
        }
        data = data[1:]
        while data:
            key, length, data = data[0:2].decode(encoding), int(data[2:4].decode(encoding)), data[4:]
            value, data = data[0:length].decode(encoding), data[length:]
            json["SE" + key.zfill(2)] = value
        return json

    def unparse(self, value, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        json = deepcopy(value)
        data = json.pop("SE00").encode(encoding)
        for key, value in sorted(json.items()):
            key = key.replace("SE", "")
            length = len(value)
            data += key.encode(encoding) + str(length).zfill(2).encode(encoding) + value.encode(encoding)
        return data, self._logicalLength(data)

    def byteLength(self, length):
        return length

    def encoding(self):
        return self._encoding or getEncoding()

    @staticmethod
    def _logicalLength(value):
        return len(value)
