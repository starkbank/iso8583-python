from binascii import hexlify, unhexlify
from copy import deepcopy


def parseString(text):
    return text


def unparseString(text):
    return text


def parseBin(text):
    return text


def unparseBin(text):
    return text


def parseBytesToBin(text, length=64):
    hexString = hexlify(text.encode("cp500"))
    binString = bin(int(hexString, 16))[2:].zfill(length)
    return binString


def unparseBytesToBin(text, length=64):
    hexString = hex(int(text, 2))[2:]
    byteString = unhexlify(hexString.zfill(length//4))
    return byteString.decode("cp500")


def parseSubelementScheme(text):
    json = {
        "SE00": text[0]
    }
    text = text[1:]
    while text:
        key, length, text = text[0:2], int(text[2:4]), text[4:]
        value, text = text[0:length], text[length:]
        json["SE" + key.zfill(2)] = value
    return json


def unparseSubelementScheme(text):
    json = deepcopy(text)
    string = json.pop("SE00")
    for key, value in sorted(json.items()):
        key = key.replace("SE00", "")
        length = len(value)
        string += key + str(length).zfill(2) + value
    return string


def parsePdsScheme(text):
    json = {}
    while text:
        key, length, text = text[0:4], int(text[4:8]), text[8:]
        value, text = text[0:length], text[length:]
        json["PDS" + key.zfill(4)] = value
    return json


def unparsePdsScheme(text):
    json = deepcopy(text)
    string = ""
    for key, value in sorted(json.items()):
        key = key.replace("PDS", "")
        length = len(value)
        string += key + str(length).zfill(4) + value
    return string
