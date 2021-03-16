from base64 import b64encode, b64decode
from copy import deepcopy
from binascii import hexlify, unhexlify
from .. import getEncoding


def parseString(text):
    return text.decode(getEncoding())


def unparseString(text):
    return text.encode(getEncoding())


def parseBin(text):
    return b64encode(text)


def unparseBin(text):
    return b64decode(text)


def parseBytesToBin(text, length=64):
    hexString = hexlify(text)
    binString = bin(int(hexString, 16))[2:].zfill(length)
    return binString


def unparseBytesToBin(text, length=64):
    hexString = hex(int(text, 2))[2:].replace("L", "")
    byteString = unhexlify(hexString.zfill(length//4))
    return byteString


def parseDE048(text):
    json = {
        "SE00": text[0:1].decode(getEncoding())
    }
    text = text[1:]
    while text:
        key, length, text = text[0:2].decode(getEncoding()), int(text[2:4].decode(getEncoding())), text[4:]
        value, text = text[0:length].decode(getEncoding()), text[length:]
        json["SE" + key.zfill(2)] = value
    return json


def unparseDE048(data):
    json = deepcopy(data)
    string = json.pop("SE00").encode(getEncoding())
    for key, value in sorted(json.items()):
        key = key.replace("SE", "")
        length = len(value)
        string += key.encode(getEncoding()) + str(length).zfill(2).encode(getEncoding()) + value.encode(getEncoding())
    return string


def parseDE112(text):
    json = {}
    while text:
        key, length, text = text[0:3].decode(getEncoding()), int(text[3:6].decode(getEncoding())), text[6:]
        value, text = text[0:length].decode(getEncoding()), text[length:]
        json["SE" + key.zfill(3)] = value
    return json


def unparseDE112(data):
    json = deepcopy(data)
    string = ""
    for key, value in sorted(json.items()):
        key = key.replace("SE", "")
        length = len(value)
        string += key.encode(getEncoding()) + str(length).zfill(3).encode(getEncoding()) + value.encode(getEncoding())
    return string


def parsePds(text):
    json = {}
    while text:
        tag, length, text = text[0:4].decode(getEncoding()), int(text[4:7].decode(getEncoding())), text[7:]
        value, text = text[0:length].decode(getEncoding()), text[length:]
        json["PDS" + tag.zfill(4)] = value
    return json


def unparsePds(json):
    byteString = b""
    for key, value in sorted(json.items()):
        tag = key.replace("PDS", "")
        length = str(len(value)).zfill(3)
        partial = tag.encode(getEncoding()) + length.encode(getEncoding()) + value.encode(getEncoding())
        if len(byteString + partial) > 999:
            break
        byteString += partial
        json.pop(key)
    return byteString
