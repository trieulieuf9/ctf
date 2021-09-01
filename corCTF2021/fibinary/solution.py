encrypted = ["10000100100", "10010000010", "10010001010", "10000100100", "10010010010", "10001000000", "10100000000", "10000100010", "00101010000", "10010010000", "00101001010", "10000101000", "10000010010", "00101010000", "10010000000", "10000101000", "10000010010", "10001000000", "00101000100", "10000100010", "10010000100", "00010101010", "00101000100", "00101000100", "00101001010", "10000101000", "10100000100", "00000100100"]
fib = [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

flag = ""
for byte in encrypted:
    char_num = 0
    for i, binary in enumerate(byte):
        if binary == "1":
            char_num += fib[i]
    flag += chr(char_num)

print(flag)