# python3 -c "print(49968*'\x00'+'\n'+32*'\x00'+'\n')" | nc mercury.picoctf.net 36981

encrypted_flag = "5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c"
key_hex = "6227295e455c7838375c7866375c7862355c786430635c7838665c7863365c78"
# convert plaintext to ord() int
# convert hex to decimal int, 2 char at a time
# XOR them to find key


def hex_to_decimal(hex):
    hex_bytes = [hex[i: i+2] for i in range(0, len(hex), 2)]
    decimals = [int(byte, 16) for byte in hex_bytes]
    return decimals


key = hex_to_decimal(key_hex)

# find flag
enc_flag_decimals = hex_to_decimal(encrypted_flag)
print(enc_flag_decimals)
print(key)
flag = list(map(lambda p, k: chr(p ^ k), enc_flag_decimals, key))
print("".join(flag))
