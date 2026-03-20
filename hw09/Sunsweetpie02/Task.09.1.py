########################################################################
#hw09.01.1

# import random
# secret_number = random.randint(1,100)

# attempts = 10 

# print("Guess the number between 1 to 100.")
# print("You have 10 attempts.")

# for i in range(1, attempts + 1):
#     guess = int(input(f"Attempt {i}: Enter your guess: "))

#     if guess == secret_number:
#         print("Congratulations! You guessed the number.")
#         break
#     elif guess < secret_number:
#         print("The secret number is bigger.")
#     else:
#         print("The secret number is smaller.")

#     if i == attempts:
#         print("You used all 10 attempts.")
#         print("The correct number was:", secret_number)

########################################################################################################
#hw09.01.2

# import pygame
# import random

# pygame.init()
# screen = pygame.display.set_mode((600, 500))
# pygame.display.set_caption("Guess the number")
# clock = pygame.time.Clock()

# title_font = pygame.font.Font(None, 45)
# text_font = pygame.font.Font(None, 25)
# input_font = pygame.font.Font(None, 50)

# BG_COLOR = (30, 30, 30)        
# TEXT_COLOR = (255, 255, 255)   
# INPUT_COLOR = (50, 200, 50)    
# HINT_COLOR = (200, 200, 0)     
# WIN_COLOR = (0, 255, 255)      
# LOSE_COLOR = (255, 50, 50)     

# secret_number = random.randint(1, 100)
# attempts_left = 10
# user_input = ""
# message = "Guess the number from 1 to 100"

# running = True
# game_over = False
# hint_message = ""

# while running:
#     screen.fill(BG_COLOR)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if not game_over:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     if user_input.isdigit():
#                         guess = int(user_input)
#                         attempts_left -= 1

#                         if guess == secret_number:
#                             message = f"Congratulations! You guessed the number."
#                             hint_message = ""
#                             game_over = True
#                         elif guess < secret_number:
#                             hint_message = f"The secret number is bigger."
#                         else:
#                             hint_message = f"The secret number is smaller."

#                         user_input = ""

#                         if attempts_left == 0 and not game_over:
#                             message = f"Game over. The correct number was: {secret_number}"
#                             hint_message = ""
#                             game_over = True
#                     else:
#                         hint_message = "Enter your guess:"
#                         user_input = ""
#                 elif event.key == pygame.K_BACKSPACE:
#                     user_input = user_input[:-1]
#                 else:
#                     if event.unicode.isdigit():
#                         user_input += event.unicode

#     title = title_font.render("Enter your guess:", True, TEXT_COLOR)
#     screen.blit(title, (120, 20))

#     msg_color = WIN_COLOR if "Congratulations" in message else LOSE_COLOR if "Game over." in message else TEXT_COLOR
#     msg_text = text_font.render(message, True, msg_color)
#     screen.blit(msg_text, (50, 100))

#     hint_text = text_font.render(hint_message, True, HINT_COLOR)
#     screen.blit(hint_text, (50, 150))

#     input_display = input_font.render(user_input, True, INPUT_COLOR)
#     screen.blit(input_display, (50, 250))

#     attempts_text = text_font.render(f"Attempts: {attempts_left}", True, TEXT_COLOR)
#     screen.blit(attempts_text, (400, 20))

#     pygame.display.update()
#     clock.tick(30)

# pygame.quit()

#########################################################################################################################