import pygame
import time
import random
pygame.init()

# defining display size
display_width = 800
display_height = 600

# defining colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (150, 0, 0)
green = (0, 255, 0)
dark_green = (0, 150, 0)

block_color = (53, 115, 255)

# defining a default ship sprite width
ship_width = 73
# defining a standard small text size for program
small_text = pygame.font.Font("freesansbold.ttf", 20)

# GLOBAL VARIABLES
pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Battleship')
clock = pygame.time.Clock()

shipImg = pygame.image.load('battleship_sprite_test.png')


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, in_color, a_color, action):
            # creating buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # print(mouse) # works! check console
    # when mouse is on button, we highlight button using mouse coordinates
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, a_color, (x, y, w, h))

        if click[0] == 1:
            action()

    else:
        pygame.draw.rect(gameDisplay, in_color, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, small_text)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)


def unpause():
    global pause
    pause = False


def pause_menu():
    while pause == True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 95)  # was 115
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        # Declaring Buttons
        button("Continue", 150, 450, 100, 50, dark_green, green, quit)
        button("Quit", 550, 450, 100, 50, dark_red, red, quit)

        pygame.display.update()
        clock.tick(15)


pause = True
pause_menu()
pygame.quit()
quit()
