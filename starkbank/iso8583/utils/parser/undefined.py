

class ParseUndefined:

    def parse(self, data, **_kwargs):
        raise ValueError("Undefined field")

    def unparse(self, value, **_kwargs):
        raise ValueError("Undefined field")

    def byteLength(self, length):
        return length
