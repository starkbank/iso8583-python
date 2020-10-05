from unittest import TestCase

from starkbank.iso8583 import parse, unparse


class TestIsoMessage(TestCase):

    def testParseUnparse(self):
        raw = "0200F238800108E0800F4000000000000000160000011319353459011000000000020000080403001305102808301308040804061234561921651028011"
        msg = parse(raw)
        self.assertEqual(raw, unparse(msg))
