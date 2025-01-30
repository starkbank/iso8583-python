from base64 import b64decode, b64encode


class ParseBin:

    def parse(self, data, **_kwargs):
        return b64encode(data)

    def unparse(self, value, **_kwargs):
        data = b64decode(value)
        logicalLength = len(data)
        return data, logicalLength

    def byteLength(self, length):
        return length
