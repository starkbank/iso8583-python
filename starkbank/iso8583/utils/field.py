

class Field:

    name = None
    lengthRule = None
    parsingRule = None

    def __init__(self, name, parsingRule, lengthRule):
        self.name = name
        self.lengthRule = lengthRule
        self.parsingRule = parsingRule

    def parse(self, data, encoding=None):
        lengthByteLength = self.lengthRule.byteLength()
        if len(data) < lengthByteLength:
            raise ValueError(
                "Expected {expected} length bytes, got {actual} in {name} for message: {message}".format(
                    expected=lengthByteLength,
                    actual=len(data),
                    name=self.name,
                    message=data,
                )
            )

        lengthData, remainingData = data[:lengthByteLength], data[lengthByteLength:]
        length = self.lengthRule.parse(data=lengthData, encoding=encoding)
        if length > self.lengthRule.limit:
            raise ValueError(
                "Expected length to be less than {limit}, got {length} in {name} for message: {message}".format(
                    limit=self.lengthRule.limit,
                    length=length,
                    name=self.name,
                    message=data,
                )
            )

        valueByteLength = self.parsingRule.byteLength(length)
        if len(remainingData) < valueByteLength:
            raise ValueError(
                "Expected {expected} value bytes, got {actual} in {name} for message: {message}".format(
                    expected=valueByteLength,
                    actual=len(remainingData),
                    name=self.name,
                    message=remainingData,
                )
            )

        valueData, remainingData = remainingData[:valueByteLength], remainingData[valueByteLength:]
        value = self.parsingRule.parse(data=valueData, length=length, encoding=encoding)
        return value, remainingData, lengthByteLength + valueByteLength

    def unparse(self, value, encoding=None):
        valueData, length = self.parsingRule.unparse(value=value, encoding=encoding)
        if length > self.lengthRule.limit:
            raise ValueError(
                "Expected length to be less than {limit}, got {length} in {name} for value: {value}".format(
                    limit=self.lengthRule.limit,
                    length=length,
                    name=self.name,
                    value=value,
                )
            )
        lengthData = self.lengthRule.unparse(value=length, encoding=encoding)

        data = lengthData + valueData
        return data
