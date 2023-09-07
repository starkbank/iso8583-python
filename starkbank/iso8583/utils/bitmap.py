from bisect import bisect_left as bisectLeft, insort


def getBitmapFields(json):
    keys = _getBitmapKeys(json=json)
    bitmapId, bitmapEnd = 0, 64
    while keys:
        index = bisectLeft(keys, bitmapEnd + 1)
        currentBitmapKeys, keys = keys[:index], keys[index:]

        nextBitmapId = _getNextBitmapId(bitmapId)
        if keys and nextBitmapId not in currentBitmapKeys:
            insort(currentBitmapKeys, nextBitmapId)

        json[getElementId(bitmapId)] = currentBitmapKeys
        bitmapId, bitmapEnd = nextBitmapId, bitmapEnd + 64
    return json


def isBitmap(elementId):
    number = _elementNumber(elementId)
    return (number % 64) == 1 or number == 0


def getElementId(number):
    return "DE" + str(number).zfill(3)


def _getNextBitmapId(bitmapId):
    if bitmapId == 0:
        return 1
    return bitmapId + 64


def _getBitmapKeys(json):
    return sorted([_elementNumber(key) for key in json.keys() if key.startswith("DE")])


def _elementNumber(elementId):
    return int(elementId.replace("DE", "").strip())
