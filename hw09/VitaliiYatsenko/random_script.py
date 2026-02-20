import random


LOVER_LIMMIT=1
HIGHTER_LIMMIT=100
MAX_ATTEMPTS = 10

print("Hi, I've chosen an integer between 1 and 100. You have 10 tries to guess. Good luck.")


random_number = random.randint(LOVER_LIMMIT,HIGHTER_LIMMIT)

attempts = MAX_ATTEMPTS
used_attempts = 0

while True:
    try:
        number = int(input('Enter an integer: '))
        if number == random_number:
            used_attempts += 1
            attempts -= 1
            print(f'Congratulation, you guessed it. The number I was thinking of {random_number}')
            print(f'The number of attempts you used:{used_attempts}')
            break
        if number < random_number:
            used_attempts += 1
            attempts -= 1
            print(f'You guessed wrong. The number I guessed is higher than yours. Attempts remaining: {attempts}')
        if number > random_number:
            used_attempts += 1
            attempts -= 1
            print(f'You guessed wrong. The number I guessed was lover than yours. Attempts remaining: {attempts}')
        if attempts == 0: 
            print( f"You've wasted all your attempts.The number I thought of is: {random_number}")
            break
    except:
        print('ERROR: Enter an integer!')
        continue
    