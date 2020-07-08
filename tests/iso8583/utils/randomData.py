from random import getrandbits


def randomBits(n=64):
    return getrandbits(n)


def randomBinary(n=64):
    return str(bin(randomBits(n)))[2:]


def randomHex(n=16):
    h = hex(randomBits(4 * n))
    if h[-1].upper() == "L":
        h = h[:-1]
    return h[2:]
