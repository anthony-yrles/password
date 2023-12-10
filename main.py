from password import password_input
from hash import hashing
from password_save import save_password

while True:
    password = password_input()
    password = hashing(password)
    print(password)
    save_password(password)
