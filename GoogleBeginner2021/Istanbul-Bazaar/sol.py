# get 624 32-bit integer
# turn them into original form
# feed into randcrack
# use randcrack to predict 31 8-bit integer to make up key
# use this key to XOR secret.enc
# get flag

from randcrack import RandCrack

with open("robo_numbers_list.txt", "r") as numbers:
    random32bits = []
    for line in numbers:
        line = line.strip().replace("-", "")
        number = int(line) - (1 << 31)
        random32bits.append(number)


with open("secret.enc", "rb") as secret:
    flag_enc = secret.read()


randcrack = RandCrack()
for i in random32bits:
    randcrack.submit(i)

keys = [randcrack.predict_getrandbits(8) for i in range(len(flag_enc))]

flag = "".join([chr(byte ^ key) for key, byte in zip(keys, flag_enc)])
print(flag)
