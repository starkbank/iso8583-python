from base64 import b64encode, b64decode
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
    encoding = getEncoding()
    json = {
        "SE00": text[0:1].decode(encoding)
    }
    text = text[1:]
    while text:
        key, length, text = text[0:2].decode(encoding), int(text[2:4].decode(encoding)), text[4:]
        value, text = text[0:length].decode(encoding), text[length:]
        json["SE" + key.zfill(2)] = value
    return json


def unparseDE048(data):
    encoding = getEncoding()
    json = data.copy()
    string = json.pop("SE00").encode(encoding)
    for key, value in sorted(json.items()):
        key = key.replace("SE", "")
        length = len(value)
        string += key.encode(encoding) + str(length).zfill(2).encode(encoding) + value.encode(encoding)
    return string


def parseDE112(text):
    encoding = getEncoding()
    json = {}
    while text:
        key, length, text = text[0:3].decode(encoding), int(text[3:6].decode(encoding)), text[6:]
        value, text = text[0:length].decode(encoding), text[length:]
        json["SE" + key.zfill(3)] = value
    return json


def unparseDE112(data):
    encoding = getEncoding()
    json = data.copy()
    string = ""
    for key, value in sorted(json.items()):
        key = key.replace("SE", "")
        length = len(value)
        string += key.encode(encoding) + str(length).zfill(3).encode(encoding) + value.encode(encoding)
    return string


def parsePds(text):
    json = {}
    while text:
        tag, length, text = text[0:4], int(text[4:7]), text[7:]
        value, text = text[0:length], text[length:]
        json["PDS" + tag.zfill(4)] = value
    return json


def unparsePds(json):
    string = ""
    for key, value in sorted(json.items()):
        tag = key.replace("PDS", "")
        length = str(len(value)).zfill(3)
        partial = tag + length + value
        if len(string + partial) > 999:
            break
        string += partial
        json.pop(key)
    return string
