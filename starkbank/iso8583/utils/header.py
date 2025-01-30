from .field import Field
from .binary import Binary
from .length import FixedLengthRule
from .parser import ParseHexadecimal, ParseBitString, ParseBitmap


class NoHeaderRule:

    def parse(self, data, json):
        return data, json

    def unparse(self, data, json):
        return b""


class VisaHeaderRule:

    subFieldByName = {}

    def __init__(self):
        self.subFieldByName = {
            subField.name: subField for subField in [
                Field(name="H01", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseHexadecimal()),
                Field(name="H02", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseHexadecimal()),
                Field(name="H03", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseHexadecimal()),
                Field(name="H04", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseHexadecimal()),
                Field(name="H05", lengthRule=FixedLengthRule(limit=3), parsingRule=ParseHexadecimal()),
                Field(name="H06", lengthRule=FixedLengthRule(limit=3), parsingRule=ParseHexadecimal()),
                Field(name="H07", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseBitString()),
                Field(name="H08", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseHexadecimal()),
                Field(name="H09", lengthRule=FixedLengthRule(limit=3), parsingRule=ParseHexadecimal()),
                Field(name="H10", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseHexadecimal()),
                Field(name="H11", lengthRule=FixedLengthRule(limit=3), parsingRule=ParseHexadecimal()),
                Field(name="H12", lengthRule=FixedLengthRule(limit=1), parsingRule=ParseHexadecimal()),
                Field(name="H13", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseBitmap(length=2, offset=13)),
                Field(name="H14", lengthRule=FixedLengthRule(limit=2), parsingRule=ParseHexadecimal()),
            ]
        }

    def parse(self, data, json):
        header, data = self._parseHeader(data)
        if _isRejectHeader(header):
            json["RejectHeader"] = header
            header, data = self._parseHeader(data)

        json["Header"] = header
        return data, json

    def _parseHeader(self, data):
        length = Binary.toInteger(data[:1])
        headerData, data = data[:length], data[length:]
        header, rejectHeader = {}, {}

        indexes = self._getHeaderIndexes()
        for index in indexes:
            if not headerData:
                break

            subField = self.subFieldByName[_subElementId(index)]
            fieldValue, headerData, _fieldLength = subField.parse(headerData)
            header.update({
                subField.name: fieldValue,
            })
            if _isBitmap(index):
                indexes.extend(fieldValue)

        return header, data

    def unparse(self, data, json):
        header = json["Header"]
        rejectHeader = json.get("RejectHeader", {})

        headerData = self._unparseHeader(header=header, messageData=data)
        rejectHeaderData = self._unparseHeader(header=rejectHeader, messageData=headerData + data)
        return rejectHeaderData + headerData

    def _unparseHeader(self, header, messageData):
        if not header:
            return b""

        header = self._addLengthPlaceholders(header=header)
        indexes = sorted(_subElementNumber(key) for key in header.keys())
        header = self._updateBitmapField(header=header, indexes=indexes)

        headerData = b""
        for index in indexes:
            subField = self.subFieldByName[_subElementId(index)]
            headerData += subField.unparse(header[subField.name])

        return self._updateLengthData(headerData, messageData)

    @classmethod
    def _addLengthPlaceholders(cls, header):
        if header:
            header.update({
                "H01": "00",
                "H04": "0000",
            })
        return header

    @classmethod
    def _updateLengthData(cls, headerData, messageData):
        headerLength, messageLength = len(headerData), len(messageData)
        binaryHeaderLength = Binary.fromInteger(headerLength, byteLength=1)
        binaryTotalLength = Binary.fromInteger(headerLength + messageLength, byteLength=2)
        return binaryHeaderLength + headerData[1:3] + binaryTotalLength + headerData[5:]

    @classmethod
    def _updateBitmapField(cls, header, indexes):
        bitmap = cls._filterBitmapIndexes(indexes)
        if not bitmap:
            return header
        header.update({
            "H13": bitmap,
        })
        return header

    @classmethod
    def _getHeaderIndexes(cls):
        return list(range(1, 14))

    @classmethod
    def _filterBitmapIndexes(cls, indexes):
        return [index for index in indexes if index > 13]


def _isBitmap(index):
    return index == 13


def _subElementId(index):
    return "H" + str(index).zfill(2)


def _subElementNumber(elementId):
    return int(elementId.replace("H", "").strip())


def _isRejectHeader(header):
    rejectGroupNumber = 14
    return rejectGroupNumber in header.get("H13", [])
