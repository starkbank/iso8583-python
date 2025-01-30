

_additionalDataElements = "DE048", "DE062", "DE123", "DE124", "DE125"


def buildPdsElement(json):
    PDS = {}
    for de in _additionalDataElements:
        PDS.update(_parsePds(json.get(de, "")))
    json.update({
        "PDS": PDS,
    })
    return json


def breakPdsElement(json):
    PDS = json.pop("PDS")
    pdsElements = iter(_additionalDataElements)
    while PDS:
        json[next(pdsElements)] = _unparsePds(PDS)
    return json


def _parsePds(text):
    json = {}
    while text:
        tag, length, text = text[0:4], int(text[4:7]), text[7:]
        value, text = text[0:length], text[length:]
        json["PDS" + tag.zfill(4)] = value
    return json


def _unparsePds(json):
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
