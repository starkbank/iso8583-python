

class Template:

    headerRule = None
    fieldByName = {}

    def __init__(self, headerRule, fields):
        self.headerRule = headerRule
        self.fieldByName = {
            field.name: field for field in fields
        }

    def getField(self, name):
        return self.fieldByName[name]

    def getHeaderRule(self):
        return self.headerRule
