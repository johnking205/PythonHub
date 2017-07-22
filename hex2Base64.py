import binascii

#hex_value = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
def hex2Base64(hexValue):
    # decode ascii hex input to binary
    binaryOutput = binascii.a2b_hex(hexValue)

    # convert bytes to base64
    return binascii.b2a_base64(binaryOutput)[:-1]
