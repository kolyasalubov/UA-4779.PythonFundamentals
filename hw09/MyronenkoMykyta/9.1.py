import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
user_input = ""
message = "Guess a number from 1 to 100"

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.unicode.isdigit():
                user_input += event.unicode

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.key == pygame.K_RETURN:
                if user_input != "":
                    guess = int(user_input)
                    attempts += 1

                    if guess == secret_number:
                        message = "You won!"
                    elif attempts >= max_attempts:
                        message = f"You lost! Number was {secret_number}"
                    elif guess > secret_number:
                        message = "Number is smaller"
                    else:
                        message = "Number is bigger"

                    user_input = ""

    # Відображення тексту
    text_surface = font.render(message, True, BLACK)
    input_surface = font.render("Your guess: " + user_input, True, BLACK)
    attempts_surface = font.render(f"Attempts: {attempts}/10", True, BLACK)

    screen.blit(text_surface, (50, 100))
    screen.blit(input_surface, (50, 150))
    screen.blit(attempts_surface, (50, 200))

    pygame.display.flip()

pygame.quit()
sys.exit()