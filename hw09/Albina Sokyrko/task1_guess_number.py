from random import randint

number = randint(1, 100)
attempts = 0
print("Вгадай число від 1 до 100!")
    
while attempts < 10:
    guess = int(input("Введіть ваше число: "))
    
    if guess < 1 or guess > 100:
        print("Число повинно бути від 1 до 100!")
        continue
    attempts += 1
            
    if guess < number:
        print("Занадто мало! Спробуйте ще раз.")
    elif guess > number:
        print("Занадто багато! Спробуйте ще раз.")
    else:
        print(f"Вітаємо! Ви вгадали число {number} за {attempts} спроб!")
        break
else:
    print(f"На жаль, ви не вгадали число {number}. Спробуйте ще раз!")