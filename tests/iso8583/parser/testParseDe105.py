from unittest import TestCase
from starkbank.iso8583.utils.parser.de105 import ParseDe105


_parser = ParseDe105(encoding="ascii")
_networkTlid = "MCw9X2kQ7rT4pL8vN3bZ1a"
_citTlid = "a7F9k3L2-Q8vB6pT1_WzYc"
_customerTlid = "Zz0Yy1Xx2Ww3Vv4Uu5Tt6S"

_rawCit = b"001022" + _networkTlid.encode()
_rawMit = b"001022" + _networkTlid.encode() + b"002022" + _citTlid.encode()
_rawLifecycle = b"001022" + _networkTlid.encode() + b"003035" + b"0010012" + b"002022" + _customerTlid.encode()

_valueCit = {"SE001": _networkTlid}
_valueMit = {
    "SE001": _networkTlid,
    "SE002": _citTlid,
}
_valueLifecycle = {
    "SE001": _networkTlid,
    "SE003": {
        "SF001": "2",
        "SF002": _customerTlid,
    },
}


class TestParseDe105Parse(TestCase):

    def testParse_cit(self):
        result = _parser.parse(_rawCit)
        self.assertEqual(result, _valueCit)

    def testParse_mitWithEconomicallyRelatedTlid(self):
        result = _parser.parse(_rawMit)
        self.assertEqual(result, _valueMit)

    def testParse_lifecycleValidationSubfields(self):
        result = _parser.parse(_rawLifecycle)
        self.assertEqual(result, _valueLifecycle)

    def testParse_tlidShapedLikeTlvStaysRawString(self):
        tlid = "001003abc002003def0030"
        result = _parser.parse(b"001022" + tlid.encode())
        self.assertEqual(result, {"SE001": tlid})

    def testParse_reservedSubElementStaysRawString(self):
        result = _parser.parse(_rawCit + b"004005ABCDE")
        self.assertEqual(result, {
            "SE001": _networkTlid,
            "SE004": "ABCDE",
        })


class TestParseDe105Unparse(TestCase):

    def testUnparse_mit_bytes(self):
        data, _logicalLength = _parser.unparse(_valueMit)
        self.assertEqual(data, _rawMit)

    def testUnparse_mit_logicalLength(self):
        _data, logicalLength = _parser.unparse(_valueMit)
        self.assertEqual(logicalLength, 56)

    def testUnparse_lifecycle_bytes(self):
        data, _logicalLength = _parser.unparse(_valueLifecycle)
        self.assertEqual(data, _rawLifecycle)

    def testUnparse_legacyRawString(self):
        data, logicalLength = _parser.unparse(_rawMit.decode())
        self.assertEqual(data, _rawMit)
        self.assertEqual(logicalLength, 56)


class TestParseDe105RoundTrip(TestCase):

    def testRoundTrip_parseUnparse(self):
        data, _logicalLength = _parser.unparse(_parser.parse(_rawLifecycle))
        self.assertEqual(data, _rawLifecycle)

    def testRoundTrip_unparseParse(self):
        result = _parser.parse(_parser.unparse(_valueLifecycle)[0])
        self.assertEqual(result, _valueLifecycle)
