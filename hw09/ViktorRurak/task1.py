import random

def random_number_game():
    number = random.randint(0,100)
    for i in range(10):
        guess = int(input("Guess a number: "))
        if guess == number:
            return "Congratulations!"
        if guess < number:
            print("Too low")
        if guess > number:
            print("Too high")
    return "Sorry, you ran out of tries"

print(random_number_game())