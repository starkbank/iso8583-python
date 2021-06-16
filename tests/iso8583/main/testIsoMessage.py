from base64 import b64decode
from unittest import TestCase
from starkbank import iso8583

iso8583.encoding = "ascii"


class TestIsoMessage(TestCase):

    def testParseUnparse(self):
        localEncoding = "cp500"
        raw64 = "AYnw8fDwdn9GASjhogrx9vXy8PT39PDw8PDw8PHw8fDw8PDw8PDw8PDw8PDw8PH18PDw8PDw8PDw8PH18PDx8vD38vPz8fT59vHw8PDw8PDw8PDw8ffy8/Px9Pnx8vD38vDx8PHy8Pfx8vD39fT5+fD18fDw8PD28PHy8/T18/f18vD09/Tw8PDw8PDx8PHwxPLw8fDx9PHy8vDx8Pj09vnw+PT28Pj18PDw8fDw8PDz8fLz9PX29/jx8vP09fb3+Pnx8vP09fbGydni40DjyMnZxEDCwdXSQEBAQEBAQOLjS0DT1uTJ4kBAQEBA1NZA8PD22fP48PHp+PTw+PTw8Pn3XyoCCECCAlgAhAegAAAABBAQlQUAAAAAAJoDIBIHnAEAnwIGAAAAABUAnxAIAQEDoAAA2sGfGgIIQJ8mCEIhVjSgssSnnycBgJ8zA+Do6J80A0QDAJ82AgIdnzcEE9Ruv/Dy9fDw8PDw8PDw8PD48PD49PD58PLx8PHy8/Tw8PnUw+Lw8fHw9tM="
        raw = b64decode(raw64)[2:]
        msg = iso8583.parse(raw, encoding=localEncoding)
        self.assertEqual(raw, iso8583.unparse(msg, encoding=localEncoding))
