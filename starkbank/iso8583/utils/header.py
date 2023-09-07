from binascii import hexlify, unhexlify


_headerProcessingRules = {
    "H1": {"length": 1},  # Header Length
    "H2": {"length": 1},  # Header Flag and Format
    "H3": {"length": 1},  # Text Format
    "H4": {"length": 2},  # Total Message Length
    "H5": {"length": 3},  # Destination ID
    "H6": {"length": 3},  # Source ID
    "H7": {"length": 1},  # Round-Trip Control Info
    "H8": {"length": 2},  # Flags
    "H9": {"length": 3},  # Message Status Flags
    "H10": {"length": 1},  # Batch Number
    "H11": {"length": 3},  # Reserved for Visa Use
    "H12": {"length": 1},  # User Information
}


def parseVisaHeader(message):  # TODO: add support to reject message headers
    headers = {}
    headerData, message = message[2:24], message[24:]

    for key, rule in sorted(_headerProcessingRules.items()):
        element, headerData = headerData[:rule["length"]], headerData[rule["length"]:]
        headers[key] = hexlify(element)

    return {"headers": headers}, message


def unparseVisaHeader(json):
    headerData = b"\x00\x00"  # reserved visa bytes
    headers = json.get("headers", {})
    for key, _rule in sorted(_headerProcessingRules.items()):
        value = headers.get(key)
        if not value:
            continue
        headerData += unhexlify(headers.get(key, ""))
    return headerData
