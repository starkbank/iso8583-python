from base64 import b64encode, b64decode
from copy import deepcopy
from binascii import hexlify, unhexlify
from starkbank import iso8583


def parseString(text):
    return text.decode(iso8583.encoding)


def unparseString(text):
    return text.encode(iso8583.encoding)


def parseBin(text):
    return b64encode(text)


def unparseBin(text):
    return b64decode(text)


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
        "SE00": text[0:1].decode(iso8583.encoding)
    }
    text = text[1:]
    while text:
        key, length, text = text[0:2].decode(iso8583.encoding), int(text[2:4].decode(iso8583.encoding)), text[4:]
        value, text = text[0:length].decode(iso8583.encoding), text[length:]
        json["SE" + key.zfill(2)] = value
    return json


def unparseSubelements(text):
    json = deepcopy(text)
    string = json.pop("SE00").encode(iso8583.encoding)
    for key, value in sorted(json.items()):
        key = key.replace("SE", "")
        length = len(value)
        string += key.encode(iso8583.encoding) + str(length).zfill(2).encode(iso8583.encoding) + value.encode(iso8583.encoding)
    return string


def parsePds(text):
    json = {}
    while text:
        key, length, text = text[0:4].decode(iso8583.encoding), int(text[4:7].decode(iso8583.encoding)), text[7:]
        value, text = text[0:length].decode(iso8583.encoding), text[length:]
        json["PDS" + key.zfill(4)] = value
    return json


def unparsePds(text):
    json = deepcopy(text)
    byteString = b""
    for key, value in sorted(json.items()):
        key = key.replace("PDS", "")
        length = str(len(value)).zfill(3)
        byteString += key.encode(iso8583.encoding) + length.encode(iso8583.encoding) + value.encode(iso8583.encoding)
    return byteString
