from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify
from .binary import Binary
from .enum import Encoding
from .. import getEncoding


def _decode(data, encoding):
    if encoding in [Encoding.cp500, Encoding.ascii]:
        return data.decode(encoding)
    if encoding == Encoding.binary:
        return data
    if encoding == Encoding.bcd:
        return hexlify(data)


def _encode(element, encoding):
    if encoding in [Encoding.cp500, Encoding.ascii]:
        return element.encode(encoding)
    if encoding == Encoding.binary:
        return element
    if encoding == Encoding.bcd:
        return unhexlify(element)


def parseString(data, encoding=None):
    return _decode(data=data, encoding=encoding or getEncoding())


def unparseString(element, encoding=None):
    return _encode(element=element, encoding=encoding or getEncoding())


def parseBin(text, encoding=None):
    return b64encode(text)


def unparseBin(element, encoding=None):
    return b64decode(element)


def parseBitString(data, encoding=None):
    hexString = hexlify(data)
    binString = bin(int(hexString, 16))[2:].zfill(8 * len(data))
    return binString


def unparseBitString(element, encoding=None):
    length = len(element)
    hexString = hex(int(element, 2))[2:].replace("L", "")
    byteString = unhexlify(hexString.zfill(length // 4))
    return byteString


def parseDE048(data, encoding=None):
    encoding = encoding or getEncoding()
    json = {
        "SE00": data[0:1].decode(encoding)
    }
    data = data[1:]
    while data:
        key, length, data = data[0:2].decode(encoding), int(data[2:4].decode(encoding)), data[4:]
        value, data = data[0:length].decode(encoding), data[length:]
        json["SE" + key.zfill(2)] = value
    return json


def unparseDE048(element, encoding=None):
    encoding = encoding or getEncoding()
    json = element.copy()
    string = json.pop("SE00").encode(encoding)
    for key, value in sorted(json.items()):
        key = key.replace("SE", "")
        length = len(value)
        string += key.encode(encoding) + str(length).zfill(2).encode(encoding) + value.encode(encoding)
    return string


def parseDE062(data, encoding=None):
    from binascii import hexlify
    print("DE062 data: {}".format(hexlify(data)))

    bitmapLength = 8
    hexString, data = hexlify(data[:bitmapLength]), data[bitmapLength:]
    binString = bin(int(hexString, 16))[2:].zfill(8 * bitmapLength)
    bitmap = Binary.toIndexes(binString)
    json = {
        "SE00": bitmap,
    }
    for index in bitmap:
        json.update({
            "SE" + str(index).zfill(2): data.decode(Encoding.cp500),
        })
    return json


def parseDE063(data, encoding=None):
    bitmapLength = 3
    hexString, data = hexlify(data[:bitmapLength]), data[bitmapLength:]
    binString = bin(int(hexString, 16))[2:].zfill(8 * bitmapLength)
    bitmap = Binary.toIndexes(binString)
    json = {
        "SE00": bitmap,
    }
    for index in bitmap:
        json.update({
            "SE" + str(index).zfill(2): hexlify(data)[-4:]
        })
    return json


def parseDE112(data, encoding=None):
    encoding = encoding or getEncoding()
    json = {}
    while data:
        key, length, data = data[0:3].decode(encoding), int(data[3:6].decode(encoding)), data[6:]
        value, data = data[0:length].decode(encoding), data[length:]
        json["SE" + key.zfill(3)] = value
    return json


def unparseDE112(element, encoding=None):
    encoding = encoding or getEncoding()
    json = element.copy()
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
