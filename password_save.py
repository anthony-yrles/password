import json

def save_password(password):
    try:
        with open("password_file.json", "r") as password_list:
            passwords = json.load(password_list)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        passwords = []
    password_check(password, passwords)
    passwords.append(password)
    with open("password_file.json", "w") as password_list:
        json.dump(passwords, password_list)


def password_check(password, passwords):
    while True:
        for i in passwords:
            if i == password:
                password = input("Ce mot de passe existe déjà veuillez en saisir un nouveau : ")
        break
