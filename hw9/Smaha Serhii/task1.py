"""
Task 1: Number Guessing Game (PyGame)
"""

import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess the Number!")
clock = pygame.time.Clock()

big_font = pygame.font.Font(None, 50)
medium_font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (200, 30, 30)
BLUE = (30, 80, 200)
GRAY = (160, 160, 160)

secret = randint(1, 100)      
attempts_left = 10           
user_input = ""              
message = ""              
message_color = BLACK
game_over = False

running = True

while running:
    clock.tick(60)  

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_over:
                if event.key == pygame.K_SPACE:
                    secret = randint(1, 100)
                    attempts_left = 10
                    user_input = ""
                    message = ""
                    message_color = BLACK
                    game_over = False
                continue 

            if event.key == pygame.K_RETURN and user_input != "":
                guess = int(user_input)
                attempts_left = attempts_left - 1

                if guess == secret:
                    message = f"You got it! The number was {secret}!"
                    message_color = GREEN
                    game_over = True
                elif attempts_left == 0:
                    message = f"No tries left! The number was {secret}"
                    message_color = RED
                    game_over = True
                elif guess > secret:
                    message = f"{guess} is too HIGH"
                    message_color = BLUE
                else:
                    message = f"{guess} is too LOW"
                    message_color = BLUE

                user_input = ""  

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.unicode.isdigit() and len(user_input) < 3:
                user_input = user_input + event.unicode

    screen.fill(WHITE)

    title = big_font.render("Guess the Number (1 - 100)", True, BLACK)
    screen.blit(title, (400 - title.get_width() // 2, 30))

    if not game_over:
        prompt = medium_font.render("Enter your guess:", True, BLACK)
        screen.blit(prompt, (400 - prompt.get_width() // 2, 120))

        box = pygame.Rect(320, 170, 160, 46)
        pygame.draw.rect(screen, (240, 240, 240), box)  
        pygame.draw.rect(screen, BLACK, box, 2)          

        typed = big_font.render(user_input, True, BLACK)
        screen.blit(typed, (box.x + 80 - typed.get_width() // 2, box.y + 6))

        att = medium_font.render(f"Attempts left: {attempts_left}", True, RED)
        screen.blit(att, (400 - att.get_width() // 2, 240))

        if message != "":
            hint = big_font.render(message, True, message_color)
            screen.blit(hint, (400 - hint.get_width() // 2, 310))

        info = small_font.render("Type a number and press ENTER", True, GRAY)
        screen.blit(info, (400 - info.get_width() // 2, 550))

    else:
        result = big_font.render(message, True, message_color)
        screen.blit(result, (400 - result.get_width() // 2, 220))

        used = medium_font.render(f"Attempts used: {10 - attempts_left}", True, BLACK)
        screen.blit(used, (400 - used.get_width() // 2, 290))

        again = small_font.render("Press SPACE to play again", True, GRAY)
        screen.blit(again, (400 - again.get_width() // 2, 550))

    pygame.display.flip()

pygame.quit()
