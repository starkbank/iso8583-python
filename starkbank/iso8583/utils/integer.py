from binascii import hexlify


class Integer:

    @classmethod
    def fromBytes(cls, byteArray):
        return int(hexlify(byteArray), 16)

    @classmethod
    def toBytes(cls, integer):
        # TODO: implement
        raise NotImplementedError()
