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

# real-world MoneySend layout: composite SE01/SE03 mixed with plain-value SE12,
# whose free text ("Homer Simpson") must not be parsed as SF TLVs
_rawMixed = b"010410105Homer0307Simpson1202041311123456789000300605021412013Homer Simpson"
_valueMixed = {
    "SE01": {
        "SF01": "Homer",
        "SF03": "Simpson",
        "SF12": "04",
        "SF13": "12345678900",
    },
    "SE03": {"SF05": "14"},
    "SE12": "Homer Simpson",
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

    def testParse_plainSubElementStaysRawString(self):
        result = _parser.parse(_rawMixed)
        self.assertEqual(result, _valueMixed)

    def testParse_plainSubElementBeforeComposite(self):
        result = _parser.parse(b"12013Homer Simpson010170113Homer Simpson")
        self.assertEqual(result, {
            "SE12": "Homer Simpson",
            "SE01": {"SF01": "Homer Simpson"},
        })

    def testParse_networkSubElementOrder(self):
        # order seen on the wire: SE01, SE12, SE03 (unparse emits sorted keys instead)
        result = _parser.parse(b"010410105Homer0307Simpson13111234567890012020412013Homer Simpson03006050214")
        self.assertEqual(result, _valueMixed)

    def testParse_qrDynamicCodeDataStaysRawString(self):
        # SE06 is plain per spec (Subfields: N/A) and can hold arbitrary QR payload
        result = _parser.parse(b"0602600021BR.GOV.BCB.PIX0114+55")
        self.assertEqual(result, {"SE06": "00021BR.GOV.BCB.PIX0114+55"})

    def testParse_ebcdicEncoding(self):
        parser = ParseDe108(encoding="cp500")
        result = parser.parse(_rawMixed.decode("ascii").encode("cp500"))
        self.assertEqual(result, _valueMixed)


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

    def testUnparse_plainSubElement_bytes(self):
        data, _logicalLength = _parser.unparse(_valueMixed)
        self.assertEqual(data, _rawMixed)

    def testUnparse_wholeElementString_bytes(self):
        data, logicalLength = _parser.unparse(_rawMixed.decode("ascii"))
        self.assertEqual(data, _rawMixed)
        self.assertEqual(logicalLength, len(_rawMixed))


class TestParseDe108RoundTrip(TestCase):

    def testRoundTrip_parseUnparse(self):
        data, _logicalLength = _parser.unparse(_parser.parse(_rawFull))
        self.assertEqual(data, _rawFull)

    def testRoundTrip_unparseParse(self):
        result = _parser.parse(_parser.unparse(_valueFull)[0])
        self.assertEqual(result, _valueFull)

    def testRoundTrip_parseUnparse_plainSubElement(self):
        data, _logicalLength = _parser.unparse(_parser.parse(_rawMixed))
        self.assertEqual(data, _rawMixed)

    def testRoundTrip_unparseParse_plainSubElement(self):
        result = _parser.parse(_parser.unparse(_valueMixed)[0])
        self.assertEqual(result, _valueMixed)
