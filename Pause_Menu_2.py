import pygame
import time
import random
import Package_Battleship
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
# defining pause background image
background_image = pygame.image.load('pause_background.jpg')
# GLOBAL VARIABLES
pause = False

# creating the menu display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Battleship')
clock = pygame.time.Clock()

# creating variable that loads a ship image
shipImg = pygame.image.load('battleship_sprite_test_Dilshawn_Sahi.png')

# function for labeling buttons
def text_objects(text, font):
    textSurface = font.render(text, True, black,)
    return textSurface, textSurface.get_rect()


# creating a button function
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

# just makes it easy to exit pause menu without quitting program
def unpause():
    global pause
    pause = False

# driver pause function
def pause_menu():
    while pause == True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(background_image, [0,0])
        largeText = pygame.font.Font('freesansbold.ttf', 95)  # was 115
        smallText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height / 8))
        gameDisplay.blit(TextSurf, TextRect)

        TextKey, KeyRect = text_objects("Hit = green, Miss = red", smallText)
        KeyRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextKey, KeyRect)

        # Declaring Buttons
        # change continue action to resume battleship
        button("Continue", 150, 450, 100, 50, dark_green, green, quit)
        button("Quit", 550, 450, 100, 50, dark_red, red, quit)

        pygame.display.update()
        clock.tick(15)


pause = True
pause_menu()
pygame.quit()
quit()
