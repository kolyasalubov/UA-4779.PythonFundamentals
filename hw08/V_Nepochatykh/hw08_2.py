import re

def is_low (pswrd: str) -> bool:    
    return re.search("[a-z]", pswrd) is not None

def is_cap (pswrd: str) -> bool:  
    return re.search("[A-Z]", pswrd) is not None

def is_dig (pswrd: str) -> bool:
    return re.search("\d", pswrd) is not None
    
def is_symb (pswrd: str) -> bool:
    return re.search("[$#@]", pswrd) is not None

def check_length (pswrd: str) -> bool:
    return 6 <= len(pswrd) <= 16
    
def is_pas_valid (pswrd: str) -> list:
    errors = []
    if not is_low(pswrd):
            errors.append("Must contain at least one lowercase char")
    if not is_cap(pswrd):
            errors.append("Must contain at least one uppercase char")
    if not is_dig(pswrd):
            errors.append("Must contain at least one digit [0-9]")
    if not is_symb(pswrd):
            errors.append("Must contain at least one special character [@#$]")
    if not check_length(pswrd):
            errors.append("Must be 8-16 characters")
    return errors

pswrd = input ("Enter your password: ")

errors = is_pas_valid(pswrd)
if not errors:
    print ("Your password is valid")
else:
    print("Your password is NOT valid:")
    for error in errors:
        print (error)
