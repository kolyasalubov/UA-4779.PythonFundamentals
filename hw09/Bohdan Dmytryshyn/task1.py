from random import randint

A = 1
B = 100
ATTEMPTS = 10

number = randint(A, B)

print(f"Guess the number between {A} and {B}. You have {ATTEMPTS} attempts.")

for i in range(ATTEMPTS):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
else:
    print(f"You're out of attempts. The number was {number}.")