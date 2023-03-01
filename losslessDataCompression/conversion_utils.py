def EncodeStringToInteger(message):
    mBytes = message.encode("utf-8")
    return int.from_bytes(mBytes, byteorder="big")

def DecodeIntegerToString(mInt):
    mBytes2 = mInt.to_bytes(((mInt.bit_length() + 7) // 8), byteorder="big")
    return mBytes2.decode("utf-8")
