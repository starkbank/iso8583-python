from unittest import TestCase
from starkbank.iso8583.utils.parser.de112 import ParseDe112


_parser = ParseDe112(encoding="ascii")
_rawSingleSe = b"001004" + b"2102"
_rawMultipleSe = b"001004" + b"2102" + b"021003" + b"21I" + b"022002" + b"02"
_valueSingleSe = {"SE001": "2102"}
_valueMultipleSe = {
    "SE001": "2102",
    "SE021": "21I",
    "SE022": "02",
}


class TestParseDe112Parse(TestCase):

    def testParse_singleSubelement(self):
        result = _parser.parse(_rawSingleSe)
        self.assertEqual(result, _valueSingleSe)

    def testParse_multipleSubelements(self):
        result = _parser.parse(_rawMultipleSe)
        self.assertEqual(result, _valueMultipleSe)

    def testParse_seKeyZeroPadded(self):
        result = _parser.parse(_rawMultipleSe)
        self.assertIn("SE001", result)
        self.assertIn("SE021", result)
        self.assertIn("SE022", result)

    def testParse_valueIsString(self):
        result = _parser.parse(_rawSingleSe)
        self.assertIsInstance(result["SE001"], str)


class TestParseDe112Unparse(TestCase):

    def testUnparse_singleSubelement_bytes(self):
        data, _logicalLength = _parser.unparse(_valueSingleSe)
        self.assertEqual(data, _rawSingleSe)

    def testUnparse_singleSubelement_logicalLength(self):
        _data, logicalLength = _parser.unparse(_valueSingleSe)
        self.assertEqual(logicalLength, 10)

    def testUnparse_multipleSubelements_bytes(self):
        data, _logicalLength = _parser.unparse(_valueMultipleSe)
        self.assertEqual(data, _rawMultipleSe)

    def testUnparse_multipleSubelements_logicalLength(self):
        _data, logicalLength = _parser.unparse(_valueMultipleSe)
        self.assertEqual(logicalLength, 27)


class TestParseDe112RoundTrip(TestCase):

    def testRoundTrip_parseUnparse(self):
        data, _logicalLength = _parser.unparse(_parser.parse(_rawMultipleSe))
        self.assertEqual(data, _rawMultipleSe)

    def testRoundTrip_unparseParse(self):
        result = _parser.parse(_parser.unparse(_valueMultipleSe)[0])
        self.assertEqual(result, _valueMultipleSe)
