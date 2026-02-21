import random
import pygame 



FPS = 60
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
ORANGE = (255, 128, 0)
BLACK = (0, 0, 0)
LIGHT_ORANGE = (255, 204, 153)
WHITE = (255, 255, 255)
COLOR_IDLE = (255, 128, 0)      
COLOR_HOVER = (255, 180, 50)
RED = (255, 0, 0)
GREEN = (0, 204, 0)


pygame.init()
SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
font = pygame.font.SysFont(None, 36)
pont = pygame.font.SysFont(None, 56)
pygame.display.set_caption("Guess the Number")
clock = pygame.time.Clock()
button_rect = pygame.Rect(545, 50, 200, 45)
sys_window = pygame.Rect(50, 170, 700, 350)
text_surf = font.render("GUESS", True, WHITE)
text_rect = text_surf.get_rect(center=button_rect.center)
user_text = "Enter a number between 1 and 100"
user_text_surf = font.render(user_text, True, BLACK)
system_text = "Press ""ENTER"" to start!"
system_text_surf = pont.render(system_text, True, BLACK)
system_text_rect = system_text_surf.get_rect(center=sys_window.center)
pygame.key.set_repeat(400, 50)
secret_number = random.randint(1, 100)
user_life = "Your life: 10"
sys_user_life = 10
user_life_surf = pont.render(user_life, True, GREEN)


def reset_game():
    global secret_number, user_life, sys_user_life, system_text, user_text, user_text_surf, user_life_surf
    secret_number = random.randint(1, 100)
    user_life = "Your life: 10"
    sys_user_life = 10
    user_text = ""
    user_text_surf = font.render(user_text, True, BLACK)
    user_life_surf = pont.render(user_life, True, GREEN)

running = True


while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                if user_text == "Enter a number between 1 and 100":
                    user_text = ""
                system_text = "Good luck!"
                system_text_surf = pont.render(system_text, True, BLACK)
                system_text_rect = system_text_surf.get_rect(center=sys_window.center)
                user_text += event.unicode
                user_text_surf = font.render(user_text, True, BLACK)
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
                user_text_surf = font.render(user_text, True, BLACK)
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                user_text = ""
                user_text_surf = font.render(user_text, True, BLACK)
            elif event.key == pygame.K_SPACE:
                reset_game()
            else:
                system_text = "Please enter a valid number!"
                system_text_surf = pont.render(system_text, True, BLACK)
                system_text_rect = system_text_surf.get_rect(center=sys_window.center)

        if event.type == pygame.MOUSEBUTTONUP:
            if sys_user_life <= 0:
                system_text = "Out of lives! Press SPACE to try again."
                system_text_surf = pont.render(system_text, True, BLACK)
                system_text_rect = system_text_surf.get_rect(center=sys_window.center)
            else:
                if event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        if user_text.isdigit():
                            val = int(user_text)
                            sys_user_life -= 1
                            if val < secret_number:
                                system_text = "Too low! Try again!"
                            elif val > secret_number:
                                system_text = "Too high! Try again!"
                            elif val == secret_number:
                                system_text = "You guessed the number!"
                                reset_game()
                        
                        user_text = ""
                    else:
                        system_text = "Please enter a valid number!"


                
                    user_text_surf = font.render(user_text, True, BLACK)
                    system_text_surf = pont.render(system_text, True, BLACK)
                    system_text_rect = system_text_surf.get_rect(center=sys_window.center)

                    
                    
                    user_life = f"Your life: {sys_user_life}"
                    life_color = GREEN
                    if sys_user_life <= 7: life_color = ORANGE
                    if sys_user_life <= 3: life_color = RED
                    user_life_surf = pont.render(user_life, True, life_color)
                    

        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(SCREEN, COLOR_HOVER, button_rect)
        else:
            pygame.draw.rect(SCREEN, COLOR_IDLE, button_rect)
    SCREEN.fill(LIGHT_ORANGE)

    
    pygame.draw.rect(SCREEN, ORANGE, sys_window)
    pygame.draw.rect(SCREEN, WHITE, (50, 45, 700, 55))
    

    color = COLOR_HOVER if button_rect.collidepoint(mouse_pos) else COLOR_IDLE

    pygame.draw.rect(SCREEN, color, button_rect, border_radius=12)
    
    SCREEN.blit(text_surf, text_rect)
    SCREEN.blit(user_text_surf, (60,55))
    SCREEN.blit(system_text_surf, system_text_rect)
    SCREEN.blit(user_life_surf, (510,530))
    
        
    



    pygame.display.update()
    clock.tick(60)
   