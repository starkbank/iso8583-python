

class Binary:

    @classmethod
    def fromHex(cls, string, length=64):
        return bin(int(string, 16))[2:].zfill(length)

    @classmethod
    def toHex(cls, binary, length=16):
        h = hex(int(binary, 2))[2:].zfill(length)
        return h if h[-1].upper() != "L" else h[:-1]

    @classmethod
    def fromIndexes(cls, indexes, length=64, offset=0):
        i = offset
        binary = ""
        for j in range(indexes[-1]):
            binary += "1" if j == i else "0"
        return "".join("1" if index in indexes else "0" for index in range(offset + 1, (length + offset + 1)))

    @classmethod
    def toIndexes(cls, binary, offset=0):
        return [index + 1 + offset for index, value in enumerate(binary) if value == "1"]
