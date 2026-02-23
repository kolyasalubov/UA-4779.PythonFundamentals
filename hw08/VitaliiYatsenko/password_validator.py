import re

password = input('Enter tour password: ')


template = r'^(?=.*[$#@])(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$#@]{6,16}$'

compile_template = re.compile(template)

if compile_template.fullmatch(password):
    print('Your password was created')
else:
    print('Your password does not meet security requirements.')