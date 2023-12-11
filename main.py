from random_choice import *
from hash import hashing
from password_save import save_password

"""
from password import password_input
La premiere partie de l'excercice, la création avec un input est dans le fichier password.py
"""

total_random = random_total()
password = random_end(total_random)
password_hashed = hashing(password)
save_password(password_hashed)
print(f"Le mot de passe généré est {password} et son hachage est {password_hashed}")
