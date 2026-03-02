import re

data = ["aD4$gt", "aD4$t", "aD45trt", "$$##@@", "aD4$gt6464TRYUE#", "aD4$gt6464TRYUE#3", "123456", "abcdefg"]

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$'

for item in data:
    result = bool(re.match(pattern, item))
    print(item, result)


