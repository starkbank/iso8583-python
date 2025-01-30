from copy import deepcopy
from ... import getEncoding


class ParseDe112:

    _encoding = None

    def __init__(self, encoding=None):
        self._encoding = encoding

    def parse(self, data, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        json = {}
        while data:
            key, length, data = data[0:3].decode(encoding), int(data[3:6].decode(encoding)), data[6:]
            value, data = data[0:length].decode(encoding), data[length:]
            json["SE" + key.zfill(3)] = value
        return json

    def unparse(self, value, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        json = deepcopy(value)
        string = ""
        for key, value in sorted(json.items()):
            key = key.replace("SE", "")
            length = len(value)
            string += key.encode(encoding) + str(length).zfill(3).encode(encoding) + value.encode(encoding)
        return string, self._logicalLength(string)

    def byteLength(self, length):
        return length

    def encoding(self):
        return self._encoding or getEncoding()

    @staticmethod
    def _logicalLength(value):
        return len(value)
