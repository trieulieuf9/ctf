from zipfile import ZipFile


with ZipFile("my_secure_files_not_for_you.zip", 'r') as zip:
    with open("/Users/trieulieuf9/Desktop/bug_bounty/bug_hunting/common_data/fuzz/wordlist/10k_common_password.txt", "r") as passwords:
        for i, password in enumerate(passwords):
            if i % 100 == 0:
                print(i)

            password = password.strip()
            try:
                zip.extractall("./", pwd=password.encode())
                print(password)
            except Exception as e:
                pass
