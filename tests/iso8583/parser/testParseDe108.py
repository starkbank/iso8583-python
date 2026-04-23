from unittest import TestCase
from starkbank.iso8583.utils.parser.de108 import ParseDe108


_parser = ParseDe108(encoding="ascii")
_rawSimple = b"010170113Homer Simpson"
_rawFull = b"010490113Homer Simpson0313Homer Simpson131112345678900"

_valueSimple = {"SE01": {"SF01": "Homer Simpson"}}
_valueFull = {
    "SE01": {
        "SF01": "Homer Simpson",
        "SF03": "Homer Simpson",
        "SF13": "12345678900",
    }
}


class TestParseDe108Parse(TestCase):

    def testParse_singleSubfield(self):
        result = _parser.parse(_rawSimple)
        self.assertEqual(result, _valueSimple)

    def testParse_multipleSubfields(self):
        result = _parser.parse(_rawFull)
        print(result)
        self.assertEqual(result, _valueFull)

    def testParse_seKeyZeroPadded(self):
        result = _parser.parse(_rawFull)
        self.assertIn("SE01", result)

    def testParse_sfKeyZeroPadded(self):
        result = _parser.parse(_rawFull)
        self.assertIn("SF01", result["SE01"])
        self.assertIn("SF03", result["SE01"])
        self.assertIn("SF13", result["SE01"])


class TestParseDe108Unparse(TestCase):

    def testUnparse_singleSubfield_bytes(self):
        data, _logicalLength = _parser.unparse(_valueSimple)
        self.assertEqual(data, _rawSimple)

    def testUnparse_singleSubfield_logicalLength(self):
        _data, logicalLength = _parser.unparse(_valueSimple)
        self.assertEqual(logicalLength, 22)

    def testUnparse_multipleSubfields_bytes(self):
        data, _logicalLength = _parser.unparse(_valueFull)
        self.assertEqual(data, _rawFull)

    def testUnparse_multipleSubfields_logicalLength(self):
        _data, logicalLength = _parser.unparse(_valueFull)
        self.assertEqual(logicalLength, 54)


class TestParseDe108RoundTrip(TestCase):

    def testRoundTrip_parseUnparse(self):
        data, _logicalLength = _parser.unparse(_parser.parse(_rawFull))
        self.assertEqual(data, _rawFull)

    def testRoundTrip_unparseParse(self):
        result = _parser.parse(_parser.unparse(_valueFull)[0])
        self.assertEqual(result, _valueFull)
