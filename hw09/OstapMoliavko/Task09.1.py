import random

answer = random.randint(1, 100)

for i in range(10):
    guess = int(input("Guess the number: "))
    if guess == answer:
        print(f"Great! You guessed the number {answer}")
        break
    print("Your number is lower than the answer" if guess < answer
          else "Your number is higher than the answer")
else:
    print("Couldn't guess the number")