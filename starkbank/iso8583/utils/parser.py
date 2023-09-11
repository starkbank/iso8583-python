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


def _parseBitmapFormat(data, bitmapLength, template):
    bitString, data = parseBitString(data[:bitmapLength]), data[bitmapLength:]
    bitmap = Binary.toIndexes(bitString)
    json = {
        "SE00": bitmap,
    }
    for index in bitmap:
        subElementId = "SE" + str(index).zfill(2)
        rule = template[subElementId]
        subElementData, data = data[:rule["limit"]], data[rule["limit"]:]  # TODO: get limit according to encoding
        json[subElementId] = rule["parser"](subElementData, encoding=rule["encoding"])  # TODO: treat padding
    return json


def _unparseBitmapFormat(element, bitmapLength, template):
    json = element.copy()
    data = b""
    indexes = []
    for subElementId in sorted(json.keys()):
        if subElementId == "SE00":
            continue
        indexes.append(int(subElementId.replace("SE", "")))
        rule = template[subElementId]
        data += rule["unparser"](json[subElementId], encoding=rule["encoding"])  # TODO: treat padding
    data = unparseBitString(Binary.fromIndexes(indexes=indexes, length=8 * bitmapLength)) + data
    return data


def parseDE062(data, encoding=None):
    return _parseBitmapFormat(data=data, bitmapLength=8, template=_de062Template)


def unparseDE062(element, encoding=None):
    return _unparseBitmapFormat(element=element, bitmapLength=8, template=_de062Template)


def parseDE063(data, encoding=None):
    return _parseBitmapFormat(data=data, bitmapLength=3, template=_de063Template)


def unparseDE063(element, encoding=None):
    return _unparseBitmapFormat(element=element, bitmapLength=3, template=_de063Template)


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


_de062Template = {
    "SE01": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE02": {"limit": 15, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE03": {"limit": 4, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE04": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE05": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE06": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE07": {"limit": 26, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE08": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE09": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE10": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE11": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE12": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE13": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE14": {"limit": 12, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE15": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE16": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE17": {"limit": 15, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE18": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE19": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE20": {"limit": 10, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE21": {"limit": 4, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE22": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE23": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE24": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE25": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE26": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
}


_de063Template = {
    "SE01": {"limit": 4, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE02": {"limit": 4, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE03": {"limit": 4, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE04": {"limit": 4, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE05": {"undefined": ""},
    "SE06": {"limit": 7, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE07": {"limit": 8, "parser": parseBitString, "unparser": unparseBitString, "encoding": Encoding.binary},
    "SE08": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE09": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE10": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE11": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE12": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE13": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE14": {"limit": 12, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE15": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE16": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE17": {"limit": 15, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE18": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE19": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE20": {"limit": 10, "parser": parseString, "unparser": unparseString, "encoding": Encoding.bcd},
    "SE21": {"limit": 4, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE22": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE23": {"limit": 2, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE24": {"limit": 6, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE25": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
    "SE26": {"limit": 1, "parser": parseString, "unparser": unparseString, "encoding": Encoding.cp500},
}