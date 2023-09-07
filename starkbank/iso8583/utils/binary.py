from binascii import hexlify, unhexlify
from sys import version_info as pyVersion


class Binary:

    @classmethod
    def fromHex(cls, hexadecimal):
        if len(hexadecimal) % 2 == 1:
            hexadecimal = "0" + hexadecimal
        return unhexlify(hexadecimal)

    @classmethod
    def toHex(cls, byteString):
        return cls._toString(hexlify(byteString))

    @classmethod
    def fromInteger(cls, number, byteLength=0):
        hexString = hex(number)[2:].replace("L", "")
        byteLength = max(byteLength, (len(hexString) + 1) // 2)
        return cls.fromHex(hexString.zfill(2 * byteLength))

    @classmethod
    def toInteger(cls, byteString):
        return int(cls.toHex(byteString), 16)

    @classmethod
    def fromBitString(cls, bitString):
        return cls.fromInteger(int(bitString, 2), byteLength=(len(bitString) + 7) // 8)

    @classmethod
    def toBitString(cls, byteString):
        return bin(cls.toInteger(byteString))[2:].zfill(8 * len(byteString))

    @classmethod
    def fromIndexes(cls, indexes, length=64, offset=0):
        binString = "".join("1" if index in indexes else "0" for index in range(offset + 1, (length + offset + 1)))
        return cls.fromBitString(binString)

    @classmethod
    def toIndexes(cls, byteString, offset=0):
        return [index + 1 + offset for index, value in enumerate(cls.toBitString(byteString)) if value == "1"]

    @classmethod
    def _toString(cls, byteString, encoding="utf-8"):
        if pyVersion.major == 2:
            return byteString
        return byteString.decode(encoding)
