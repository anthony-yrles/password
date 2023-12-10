import json

def save_password(password):
    try:
        with open("password_file.json", "r") as password_list:
            passwords = json.load(password_list)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        passwords = []
    passwords.append(password)
    with open("password_file.json", "w") as password_list:
        json.dump(passwords, password_list)
