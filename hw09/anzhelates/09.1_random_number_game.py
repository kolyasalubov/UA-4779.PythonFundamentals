import random

secret_num = random.randint(1,100)
guess_count = 0

while guess_count < 10:
    print("Enter your guess: ")
    guess = int(input())
    guess_count += 1
    if guess == secret_num:
        print("You've guessed it")
        break
    elif guess < secret_num:
        print("The random number is bigger")
    else:
        print("The random number is smaller")

else:
    print("Out of guesses, the secret number was: ", secret_num)