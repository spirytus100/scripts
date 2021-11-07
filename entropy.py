import math
import getpass

passwd = getpass.getpass("Podaj hasło: ")

small_letters = "abcdefghjiklmnopqrstuvwxyz"
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_signs = """~`!@#$%^&*()_+-=[]{};':",./<>?\|"""

small = []
big = []
num = []
special = []
for letter in passwd:
    if letter in small_letters:
        small.append(letter)
    elif letter in big_letters:
        big.append(letter)
    elif letter in numbers:
        num.append(letter)
    elif letter in special_signs:
        special.append(letter)
        
setsize = 0
setdict = {"małe": small, "duże":big, "cyfry": num, "specjalne": special}
for key, val in setdict.items():
    if len(val) > 0:
        if key == "małe":
            setsize = setsize + len(small_letters)
        elif key == "duże":
            setsize = setsize + len(big_letters)
        elif key == "cyfry":
            setsize = setsize + len(numbers)
        elif key == "specjalne":
            setsize = setsize + len(special_signs)
        
set_log = round(math.log(setsize, 2), 2)
strength = round(len(passwd) * set_log, 2)
brute_force = int(round(2 ** strength, 0))

print("Wielkość zbioru znaków wykorzystanych w haśle:", setsize)
print("Hasło ma siłę", strength, "bitów entropii.")
print("Maksymalna liczba kombinacji potrzebna do złamania hasła: {:,}".format(brute_force))
