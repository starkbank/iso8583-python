

class ParseBitmapFormat:

    subFieldByName = {}

    def __init__(self, subFields):
        self.subFieldByName = {
            field.name: field
            for field in subFields
        }

    def parse(self, data, **_kwargs):
        json = {}
        indexes = [0]
        for index in indexes:
            elementId = _subElementId(index)
            value, data, _byteLength = self.subFieldByName[elementId].parse(data=data)
            json[elementId] = value
            if _isBitmap(index):
                indexes.extend(value)
        return json

    def unparse(self, value, **_kwargs):
        data, value = b"", value.copy()
        value["SE00"] = []
        indexes = [_subElementNumber(key) for key in sorted(value.keys())]
        value["SE00"] = [index for index in indexes if not _isBitmap(index)]
        for index in indexes:
            subElementId = _subElementId(index)
            subField = self.subFieldByName[subElementId]
            data += subField.unparse(value=value[subElementId])
        return data, len(data)

    def byteLength(self, length):
        return length


def _subElementId(number):
    return "SE" + str(number).zfill(2)


def _subElementNumber(id):
    return int(id.replace("SE", "").strip())


def _isBitmap(index):
    return index == 0
