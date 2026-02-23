import re

def validate_pass(password):
    if len(password) < 6:
        return ("Password must be at least 6 characters long.")
    if not re.search(r'[A-Z]', password):
        return ("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        return ("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        return ("Password must contain at least one digit.")
    if not re.search(r'[$#@]', password):
        return ("Password must contain at least one special character from [$#@].")
    return ("Password is valid.")

password = input("Enter a password: ")
print(validate_pass(password))

####################
# Alternative solution:

import re

def validate_pass(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,}$'
    
    if re.match(pattern, password):
        return "Password is valid."
    else:
        return "Password is invalid."

password = input("Enter a password: ")
print(validate_pass(password))