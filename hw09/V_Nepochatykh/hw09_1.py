import pygame
import random

pygame.init()

display_width = 800
display_height = 400

white =(255,255,255)
grey = (200,200,200)
light_green = (175,245,162)
black = (0, 0, 0)
red = (143, 33, 3)
FPS = 30
done = False
active_color = grey

tries = 0
user_input = ''
input_active = False
status = ''
wrong_field = False
history = []
history_y = 100
numb_to_guess = random.randint(0, 100)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Guess number')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25, True, False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and tries == 0:
                tries = 1
                input_active = True
                active_color = light_green
            if 0 < tries <= 10 and status != '=':
                if event.key == pygame.K_RETURN:
                    input_active = not input_active
                    if input_active:
                        active_color = light_green
                        user_input = ''
                        tries += 1
                    if not input_active:
                        if user_input == '' or not (0<= int(user_input)<=100):
                            input_active = not input_active
                            wrong_field = True
                        else:
                            active_color = grey
                            wrong_field = False
                            if int(user_input) > numb_to_guess:
                                status = '<'
                            elif int(user_input) < numb_to_guess:
                                status = '>'
                            else:
                                status = '='
                            history.insert (0, f"X {status} {user_input}" )
                elif input_active:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.unicode.isdigit() and len(user_input) < 3:                    
                        user_input += event.unicode

    
    
    start_text = font.render("Try to guess number from 0 to 100 in 10 tries", True, black)
    press_s_text = font.render("Press S to start the game ", True, black)
    tries_left_text = font.render(f"It's your {tries} try. Enter a number and press Enter", True, black)
    your_numb_text = font.render(f"Your number:  {user_input} ", True, black)
    wrong_field_text = font.render("Number from 0 to 100 is needed" , True, red)
    lose_text = font.render(f"YOU LOST :(", True, black)
    win_text = font.render(f"X = {user_input}! YOU WON IN {tries} TRIES!!!", True, black)
    gameDisplay.fill(white)


    if tries == 0:
        gameDisplay.blit(start_text, [20, 20])
        gameDisplay.blit(press_s_text, [20, 50])
    elif 0<tries<=10:
        if status == '=':
            gameDisplay.blit(win_text, [20, 60]) 
        else:
            pygame.draw.rect(gameDisplay, active_color, (195, 60, 50, 30))
            gameDisplay.blit(tries_left_text, [20, 20])
            gameDisplay.blit(your_numb_text, [20, 60]) 
            for i in range (len(history)):
                history_y = 100 + 30*i
                gameDisplay.blit(font.render(history[i], True, black), [20, history_y])  
            if wrong_field:
                gameDisplay.blit(wrong_field_text, [255, 60])               
    elif tries == 11:
        gameDisplay.blit(lose_text, [20, 60])  

    pygame.display.update()
    clock.tick(FPS)