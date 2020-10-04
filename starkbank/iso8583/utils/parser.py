from binascii import hexlify


def parseString(text):
    return text


def parseBin(text):
    return text


def parseHexToBin(text, length=64):
    return bin(int(text, 16))[2:].zfill(length)


def parseBytesToBin(text, length=64):
    return parseHexToBin(text=hexlify(text.encode("cp500")), length=length)


def parseDE048Scheme(text):
    json = {
        "SE00": text[0]
    }
    text = text[1:]
    while text:
        key, length, text = text[0:2], int(text[2:4]), text[4:]
        value, text = text[0:length], text[length:]
        json["SE" + key.zfill(2)] = value
    return json
