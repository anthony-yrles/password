def password_input():
    autorized_Special_Char = "!@#$%^&*"
    password = input("Veuillez saisir votre nouveau password: ")
    while True:
        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in autorized_Special_Char for char in password) or not any(char.isdigit() for char in password):
            password = input("Veuillez saisir un mot de passe valide : ")
        else:
            print(f"Mot de passe {password} enregistré")
            return(password) 
        
password = password_input()
print(password)