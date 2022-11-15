import random

lc_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

uc_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

special_chars = ['"', "£", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "{", "}", "[", "]", "@", "#", "?", "!", "'", "~", ".", ",", "<", ">", "/"]

number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

error_stmt = "Please apply the minimum characters for each section. Try again"

#collect password specifications based on specified categories
lc_choice = int(input("How many Lower Case characters? (4 minimum) "))
# collect password specifications in a way that ensures unfulfilled requirement end the script
if lc_choice >= 4:
    lc = random.choices(lc_letters, k = lc_choice)
    uc_choice = int(input("How many Upper Case characters? (2 minimum) "))
    if uc_choice >= 2:
        uc = random.choices(uc_letters, k = uc_choice)
        spc_choice = int(input("How many Special characters? (1 minimum) "))
        if spc_choice >= 1:
            spc = random.choices(special_chars, k = spc_choice)
            num_choice = int(input("How many Numerical characters? (1 minimum) "))
            if num_choice >= 1:
                num = random.choices(number_list, k = num_choice)
                combo = lc + uc + spc + num
                print(combo)
# Randomise list items and create the password as a single string                
                random.shuffle(combo)
                passgen = ''.join(combo)
                print(passgen)
# Control for non-compliance of character requirements
            else:
                print(error_stmt)
        else:
            print(error_stmt)
    else:
        print(error_stmt)
else:
    print(error_stmt)
