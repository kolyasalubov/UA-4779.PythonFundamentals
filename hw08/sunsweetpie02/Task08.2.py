##############################################

import re

Password = input("Enter the password: ")
valid = all([
  6 <= len(Password) <= 16,
  bool(re.search(r"[a-z]", Password)),
  bool(re.search(r"[A-Z]", Password)),
  bool(re.search(r"[0-9]", Password)),
    bool(re.search(r"[$#@]", Password))
])

print("The password is valid" if valid else "The password is")

####################################################################