from ... import getEncoding


class ParseString:

    _encoding = None

    def __init__(self, encoding=None):
        self._encoding = encoding

    def parse(self, data, encoding=None, **_kwargs):
        return _decode(data, encoding=encoding or self.encoding())

    def unparse(self, value, encoding=None, **_kwargs):
        length = self._logicalLength(value)
        return _encode(value, encoding=encoding or self.encoding()), length

    def byteLength(self, length):
        return length

    def encoding(self):
        return self._encoding or getEncoding()

    @staticmethod
    def _logicalLength(value):
        return len(value)


def _decode(data, encoding):
    return data.decode(encoding)


def _encode(value, encoding):
    return value.encode(encoding)
