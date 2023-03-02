def EncodeStringToInteger(message):
    mBytes = message.encode("utf-8")
    return int.from_bytes(mBytes, byteorder="big")
