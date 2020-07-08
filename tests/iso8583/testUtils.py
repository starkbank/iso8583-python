from starkbank.iso8583.utils import binary
from unittest import TestCase, main

from starkbank.iso8583.utils.binary import Binary
from tests.iso8583.utils.randomData import randomBits, randomHex


class TestBinaryUtils(TestCase):

    def test_everything(self):
        for _ in range(1000):
            randomsequence = randomHex(max(randomBits(4), 1))
            indexes = Binary.toIndexes(Binary.fromHex(randomsequence))
            answer = Binary.toHex(Binary.fromIndexes(indexes))
            n = len(randomsequence)
            self.assertEqual(randomsequence, answer[-n:])