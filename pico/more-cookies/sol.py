from base64 import b64decode, b64encode
import requests

# why do i decode twice?
# because they encode they encode their cookie twice!!
def bit_flip(pos, bit, data):
    raw = b64decode(b64decode(data))
    byte_list = bytearray(raw)
    byte_list[pos] = byte_list[pos] ^ bit
    return b64encode(b64encode(byte_list)).decode()


def main():
    cookie = "NE5pZjcwMDd1WU81VDV5VHlUcUorTW1tMSttWmhyK0Y5dmpLTVZXdXEzS3pHWGhRSW1XUUUwU3A5MzIvK0NpVVNzQXhERmQ1dXNYK0U0YnFRaG12KytlN21OSEJDbnVsTml3cmkzNnZKRmpMQStHcGV2Mml4TFRyNlNvRDMxSUs="
    for i in range(128):
        coo = bit_flip(i, 1, cookie)
        cookies = {'auth_name': coo}
        r = requests.get('http://mercury.picoctf.net:34962/', cookies=cookies)
        print(i, r.status_code)
        if "picoCTF{" in r.text:
          print(r.text)
          break

main()
