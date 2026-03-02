#----------------------------------------------------------------
# Funkce ověří zda je uživatel dospělý
#----------------------------------------------------------------
def is_adult(age: int)-> bool:
    """Funkcia, ktora overi ci je uzivatel dospely

    Args:
        age (int): vek uzivatela

    Returns:
        bool: True ak je dospely inak False"""
    if age is None:
        return False
    elif age >= 18:
        return True
    else:
        return False

#--------------------------------------------------------------
#Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
#----------------------------------------------------------------
def is_name_valid(username: str)-> bool:
    """Funkcia ktora overi ci uzivatelske meno ma aspon 4 znaky

    Args:
        username (str): uzivatelske meno

    Returns:
        bool: True ak ma minimalne 4 znaky inak False"""
    if username is None:
        return False
    elif len(username)>=4:
        return True
    else:
        return False

#---------------------------------------------------------------------------
#Funkce vytvoří slovník reprezentujícího uživatele.
#Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
#---------------------------------------------------------------------------
def create_user( username: str,age: int ,email: str)-> dict:
    """Funkcia vytvori slovnik reprezentujuci uzivatela
    Args:
        username (str): uzivateslke meno
        age (int): vek uzivatela
        email (str): email uzivatela

    Returns:
        dist: vytvori, dokumentuje a validuje uzivatela"""
    user={}
    user_info={}
    is_adult_var=is_adult(age)
    is_name_valid_var=is_name_valid(username)
    if(is_adult_var and is_name_valid_var):
        user["success"]=True
        user_info["username"]=username
        user_info["age"]=age
        user_info["email"]=email
        user["user"]=user_info
    else:
        user["success"] = False
        if is_adult_var:
            user["error"] = "Error: Meno ma menej ako 4 znaky"
        elif is_name_valid_var:
            user["error"]="Error: User nie je plnolety"
        else:
            user["error"]="Error: Meno ma menej ako 4 znaky a user nie je plnolety."
    return user

#------------------------------------------------------------------------------------------------------------------------------
#Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření
#------------------------------------------------------------------------------------------------------------------------------
def print_user_info(user: dict)->None:
    """Funkcia vypise uzivatela do konzole
    Args:
        user (dict): vytvoreny uzivatel

    Returns:
        None"""
    print(user)

#------------------------------------------------------------------------------------------------------------
# Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.
#-----------------------------------------------------------------------------------------------------------
users=[]
users.append(create_user("Adam", 40,"adam@adam.sk"))
users.append(create_user("Juraj", 12, "juraj@juraj.sk"))
users.append(create_user("Eva", 45,"eva@eva.sk"))
users.append(create_user("Marek", 63,"marek@marek.sk"))

for user in users:
    print_user_info(user)