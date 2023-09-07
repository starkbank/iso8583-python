from ..binary import Binary


class ParseBitmap:

    _length = 8
    offset = 0

    def __init__(self, offset=0, length=8):
        self.offset = offset
        self._length = length

    def parse(self, data, **_kwargs):
        return Binary.toIndexes(byteString=data, offset=self.offset)

    def unparse(self, value, **_kwargs):
        data = Binary.fromIndexes(indexes=value, offset=self.offset, length=8 * self._logicalLength())
        return data, self._logicalLength()

    def byteLength(self, length):
        return length

    def _logicalLength(self):
        return self._length
