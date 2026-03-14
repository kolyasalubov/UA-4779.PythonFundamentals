def check_age(age):
    if age <= 0:
        raise ValueError("age must be greater than 0")
    return "Your age is even" if age % 2 == 0 else "Your age is odd"

try:
    user_age = int(input("Enter your age: "))
    print(check_age(user_age))
except ValueError as e:
    print(f"Input error: {e}")