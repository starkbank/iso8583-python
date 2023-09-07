from unittest import TestCase
from starkbank.iso8583.utils.parser import _encode, _decode


class TestEncoding(TestCase):

    def testEncodeDecodeCp500(self):
        localEncoding = "cp500"
        data = "testString".encode(localEncoding)
        self.assertEqual(_encode(_decode(data, encoding=localEncoding), encoding=localEncoding), data)

    def testEncodeDecodeAscii(self):
        localEncoding = "ascii"
        data = "testString".encode(localEncoding)
        self.assertEqual(_encode(_decode(data, encoding=localEncoding), encoding=localEncoding), data)

    def testEncodeDecodeBinary(self):
        localEncoding = "binary"
        data = b"\xaa\xbb\xcc\xdd\xee\xff"
        self.assertEqual(_encode(_decode(data, encoding=localEncoding), encoding=localEncoding), data)

    def testEncodeDecodeBcd(self):
        localEncoding = "binary"
        data = b"\x12\x34\x56\x78\x90"
        self.assertEqual(_encode(_decode(data, encoding=localEncoding), encoding=localEncoding), data)
