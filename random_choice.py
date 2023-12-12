import random

def random_int():
    """"
    Selection d'un nombre randomisé random_range d'int dans le tableau int-list
    """
    random_range = random.randint(3, 9)
    int_list = ["0","1","2","3","4","5","6","7","8","9"]
    int_choice = random.choices(int_list, k = random_range)
    return(int_choice)

def random_lower():
    """"
    Selection d'un nombre randomisé random_range d'int dans le tableau lower_list
    """
    random_range = random.randint(3, 9)
    lower_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lower_choice = random.choices(lower_list, k = random_range)
    return(lower_choice)

def random_upper():
    """"
    Selection d'un nombre randomisé random_range d'int dans le tableau upper_list
    """
    random_range = random.randint(3, 9)
    upper_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    upper_choice = random.choices(upper_list, k = random_range)
    return(upper_choice)

def random_special_character():
    """"
    Selection d'un nombre randomisé random_range d'int dans le tableau special_list
    """
    random_range = random.randint(1, 2)
    special_list = ["!","@","#","$","%","^","&","*"]
    special_choice = random.choices(special_list, k = random_range)
    return(special_choice)

def random_total():
    """"
    Appel de toutes les fonction de randomisation et réunion dans un seul tableau total_random
    """
    int_choice = random_int()
    lower_choice = random_lower()
    upper_choice = random_upper()
    special_choice = random_special_character()
    total_random = int_choice + lower_choice + upper_choice + special_choice
    return(total_random)

def random_end(total_random):
    """"
    randomisation de l'ordre de total_random puis création d'une string password
    """
    password = ""
    random.shuffle(total_random)
    for i in total_random:
        password = password + i
    return(password)


