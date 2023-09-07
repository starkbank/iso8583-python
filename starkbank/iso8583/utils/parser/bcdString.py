from ..binary import Binary


class ParseBcdString:

    def parse(self, data, length, **_kwargs):
        return Binary.toHex(data)[-length:]

    def unparse(self, value, **_kwargs):
        length = self._logicalLength(value)
        return Binary.fromHex(value), length

    def byteLength(self, length):
        return (length + 1) // 2

    @staticmethod
    def _logicalLength(value):
        return len(value)
