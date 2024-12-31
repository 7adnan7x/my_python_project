import random
import string

def password_generator(min_length , number=True , special_char = True):
    letter = string.ascii_letters
    digit = string.digits
    special = string.punctuation

    character = letter
    if number:
        character += digit
    if special_char:
        character += special
    
    pwd =""
    meet_critaria = False
    has_number = False
    has_special = False

    while not meet_critaria or len(pwd) < min_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digit:
            has_number= True
        elif new_char in special:
            has_special = True
        
        meet_critaria = True
        if number:
            meet_critaria = has_number
        if special_char:
            meet_critaria = meet_critaria and has_special
        
    return pwd
while True:

    pass_length = int(input("enter the number you want as password"))
    hav_number= input("do you want a number in it(y/n)").lower() == "y"
    hav_special_char = input("d0 you want special charater (y/n)").lower() == "y"
    man =password_generator(pass_length, hav_number, hav_special_char)
    print(man)