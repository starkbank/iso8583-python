from ..binary import Binary


class ParseBitString:

    def parse(self, data, **_kwargs):
        return Binary.toBitString(data)

    def unparse(self, value, **_kwargs):
        return Binary.fromBitString(value), self._logicalLength(value)

    def byteLength(self, length):
        return length

    @staticmethod
    def _logicalLength(value):
        return len(value) // 8
