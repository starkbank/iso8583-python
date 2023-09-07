from binascii import hexlify, unhexlify
from .enum import Encoding, LengthType


def getLengthBytesLength(lengthType, encoding):
    return {
        LengthType.fixed: {
            Encoding.ascii: 0,
            Encoding.cp500: 0,
            Encoding.binary: 0,
            Encoding.bcd: 0,
        },
        LengthType.lvar: {
            Encoding.ascii: 1,
            Encoding.cp500: 1,
            Encoding.binary: 1,
            Encoding.bcd: 1,
        },
        LengthType.llvar: {
            Encoding.ascii: 2,
            Encoding.cp500: 2,
            Encoding.binary: 1,
            Encoding.bcd: 1,
        },
        LengthType.lllvar: {
            Encoding.ascii: 3,
            Encoding.cp500: 3,
            Encoding.binary: 2,  # TODO: this should be 2, but Visa uses only 1 byte to indicate lllvar fields with length smaller than or equal to 255
            Encoding.bcd: 2,
        },
        LengthType.llllvar: {
            Encoding.ascii: 4,
            Encoding.cp500: 4,
            Encoding.binary: 2,
            Encoding.bcd: 2,
        },
    }[lengthType][encoding]


def parseLength(lengthData, lengthEncoding):
    if lengthEncoding in [Encoding.cp500, Encoding.ascii]:
        return int(lengthData.decode(lengthEncoding))
    if lengthEncoding == Encoding.binary:
        return int(hexlify(lengthData), 16)
    if lengthEncoding == Encoding.bcd:
        return int(hexlify(lengthData))
    raise Exception("Unknown length encoding: {lengthEncoding}")


def unparseLength(length, lengthType, lengthEncoding):
    data = b""
    paddingChar = b""
    if lengthType == LengthType.fixed:
        return data

    if lengthEncoding in [Encoding.cp500, Encoding.ascii]:
        paddingChar = "0".encode(lengthEncoding)
        data = str(length).encode(lengthEncoding)
    if lengthEncoding == Encoding.binary:
        paddingChar = b"\x00"
        hexString = hex(length)[2:].replace("L", "")
        data = unhexlify(hexString.zfill(len(hexString) + len(hexString) % 2))
    if lengthEncoding == Encoding.bcd:
        paddingChar = b"\x00"
        bcdString = str(length)
        data = unhexlify(bcdString.zfill(len(bcdString) + len(bcdString) % 2))

    paddingBytes = paddingChar * (getLengthBytesLength(lengthType=lengthType, encoding=lengthEncoding) - len(data))
    return paddingBytes + data


def getDataLengthFromDataEncoding(parseSize, dataEncoding):
    return (parseSize // 2) + (parseSize % 2) if dataEncoding == Encoding.bcd else parseSize
