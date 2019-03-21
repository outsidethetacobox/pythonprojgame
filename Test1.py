import math
import pygame
pygame.init()

print()
print()
print()
# Dilshawn Sahi em8654

gameDisplay = pygame.display.set_mode((1100, 750))
pygame.display.set_caption('Battleship!')
clock = pygame.time.Clock()

display_width = 800
display_height = 600

# declaring ship sprite
ship_image = pygame.image.load('battleship_sprite_test.png')
# declaring board background image
board_image = pygame.image.load('grid.png')

crashed = False

# declaring colors
black = (0, 0, 0)
white = (255, 255, 255)


x = (display_width * 0.02)
y = (display_height * 0.02)
X = display_width
Y = display_height

# function to display ship sprite


def ship(x, y):
    gameDisplay.blit(ship_image, (x, y))


def board(X, Y):
    gameDisplay.blit(board_image, (X, Y))


# displaying pygame
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    # gameDisplay.fill(black)
    board(X, Y)
    ship(x, y)
    ship(x * 15.5, y)
    ship(x * 30, y)
    print(event)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -5
        elif event.key == pygame.K_RIGHT:
            x_change = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()

print()
print()
print()
print()
