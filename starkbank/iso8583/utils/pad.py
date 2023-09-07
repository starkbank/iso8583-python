

def unpadBcdString(element, length):
    return element[-length:]


def padBcdString(element):
    return "0" * (len(element) % 2) + element, len(element) % 2
