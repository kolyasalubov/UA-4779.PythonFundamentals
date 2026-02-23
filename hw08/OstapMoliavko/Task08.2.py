special_chars = ['$','#','@']
err_msg = "Invalid password: "
pwd = input("Enter your password: ")

if (len(pwd) >= 6 and len(pwd) <= 16
        and any(c.isalpha() for c in pwd)
        and any(c.isdigit() for c in pwd)
        and any(c in pwd for c in special_chars)):
    print("Your password is accepted")
else:
    if len(pwd) < 6:
        err_msg += "\nYour password is too short, should be at least 6 characters"
    elif len(pwd) > 16:
         err_msg += "\nYour password is too long, should be at most 16 characters"
    if not any(c.isalpha() for c in pwd):
        err_msg += "\nYour password should contain letters"
    if not any(c.isdigit() for c in pwd):
        err_msg += "\nYour password should contain numbers"
    if not any(c in pwd for c in special_chars):
        err_msg += "\nYour password should contain at least one of these characters: $, # or @"

    print(err_msg)