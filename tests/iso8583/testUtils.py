from unittest import TestCase
from starkbank.iso8583.utils.binary import Binary
from tests.iso8583.utils.randomData import randomBits, randomHex


class TestBinaryUtils(TestCase):

    def test_everything(self):
        for _ in range(1000):
            randomsequence = randomHex(max(randomBits(4), 1))
            while not randomsequence.replace("0", ""):
                randomsequence = randomHex(max(randomBits(4), 1))

            binary = Binary.fromHex(randomsequence)
            indexes = Binary.toIndexes(binary)
            answer = Binary.toHex(Binary.fromIndexes(indexes, length=8 * len(binary)))
            n = len(randomsequence)
            self.assertEqual(randomsequence, answer[-n:])
