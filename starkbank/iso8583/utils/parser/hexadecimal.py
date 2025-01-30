from ..binary import Binary


class ParseHexadecimal:

    def parse(self, data, **_kwargs):
        return Binary.toHex(data)

    def unparse(self, value, **_kwargs):
        logicalLength = self._logicalLength(value)
        return Binary.fromHex(value), logicalLength

    def byteLength(self, length):
        return length

    @staticmethod
    def _logicalLength(value):
        return len(value) // 2
