from binascii import hexlify, unhexlify
from copy import deepcopy
from starkbank.iso8583 import encoding


def parseString(text):
    return text.decode(encoding)


def unparseString(text):
    return text.encode(encoding)


def parseBin(text):
    return text


def unparseBin(text):
    return text


def parseBytesToBin(text, length=64):
    hexString = hexlify(text)
    binString = bin(int(hexString, 16))[2:].zfill(length)
    return binString


def unparseBytesToBin(text, length=64):
    hexString = hex(int(text, 2))[2:]
    byteString = unhexlify(hexString.zfill(length//4))
    return byteString


def parseSubelements(text):
    json = {
        "SE00": text[0:1].decode(encoding)
    }
    text = text[1:]
    while text:
        key, length, text = text[0:2].decode(encoding), int(text[2:4].decode(encoding)), text[4:]
        value, text = text[0:length].decode(encoding), text[length:]
        json["SE" + key.zfill(2)] = value
    return json


def unparseSubelements(text):
    json = deepcopy(text)
    string = json.pop("SE00").encode(encoding)
    for key, value in sorted(json.items()):
        key = key.replace("SE", "")
        length = len(value)
        string += key.encode(encoding) + str(length).zfill(2).encode(encoding) + value.encode(encoding)
    return string


def parsePds(text):
    json = {}
    while text:
        key, length, text = text[0:4].decode(encoding), int(text[4:7].decode(encoding)), text[7:]
        value, text = text[0:length].decode(encoding), text[length:]
        json["PDS" + key.zfill(4)] = value
    return json


def unparsePds(text):
    json = deepcopy(text)
    byteString = b""
    for key, value in sorted(json.items()):
        key = key.replace("PDS", "")
        length = str(len(value)).zfill(3)
        byteString += key.encode(encoding) + length.encode(encoding) + value.encode(encoding)
    return byteString
