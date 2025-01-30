from .binary import Binary
from .enum import Encoding
from .. import getEncoding


class FixedLengthRule:

    limit = 0

    def __init__(self, limit):
        self.limit = limit

    def parse(self, data, **_kwargs):
        return self.limit

    def unparse(self, value, **_kwargs):
        return b""

    def byteLength(self):
        return 0


class VariableLengthRule:

    _byteLength = 0
    _encoding = None
    limit = 0

    def __init__(self, limit, byteLength, encoding=None):
        self.limit = limit
        self._byteLength = byteLength
        self._encoding = encoding

    def parse(self, data, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        return {
            Encoding.ascii: _parseAsciiLength,
            Encoding.cp500: _parseCp500Length,
            Encoding.binary: _parseBinaryLength,
        }[encoding](data)

    def unparse(self, value, encoding=None, **_kwargs):
        encoding = encoding or self.encoding()
        return {
            Encoding.ascii: _unparseAsciiLength,
            Encoding.cp500: _unparseCp500Length,
            Encoding.binary: _unparseBinaryLength,
        }[encoding](value=value, byteLength=self.byteLength())

    def byteLength(self):
        return self._byteLength

    def encoding(self):
        return self._encoding or getEncoding()


def _parseBinaryLength(data):
    return Binary.toInteger(data)


def _parseAsciiLength(data):
    return _parseEncodedLength(data, encoding=Encoding.ascii)


def _parseCp500Length(data):
    return _parseEncodedLength(data, encoding=Encoding.cp500)


def _parseEncodedLength(data, encoding):
    return int(data.decode(encoding))


def _unparseBinaryLength(value, byteLength):
    return Binary.fromInteger(value, byteLength=byteLength)


def _unparseAsciiLength(value, byteLength):
    return _unparseEncodedLength(value=value, byteLength=byteLength, encoding=Encoding.ascii)


def _unparseCp500Length(value, byteLength):
    return _unparseEncodedLength(value=value, byteLength=byteLength, encoding=Encoding.cp500)


def _unparseEncodedLength(value, byteLength, encoding):
    data = str(value).encode(encoding)
    padding = "0".encode(encoding) * (byteLength - len(data))
    return padding + data
