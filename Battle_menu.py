import pygame

pygame.init()
clock = pygame.time.Clock()
black = 0, 0, 0
blue = 0, 0, 255
violet_blue = 138, 43, 226
red = 255, 0, 0
dar_red = 139, 0, 0
clock = pygame.time.Clock()
Display = pygame.display.set_mode((800, 700))
F = pygame.font.SysFont("Times New Norman", 24)
LG_F = pygame.font.SysFont("Time New Norman", 115)
title = LG_F.render("BattleShip", True, blue)
classic = F.render("Classic Mode", True, black)
new = F.render("Salvo mode", True, black)
C_button = pygame.Rect(200, 600, 100, 50)
N_button = pygame.Rect(400, 600, 100, 50)
Title = pygame.Rect(500, 500, 200, 100)
pygame.display.set_caption('BattleshipS')
bg = pygame.image.load("pics/battleshipbackround.jpg")


# text , rect , color, hover color, x, h, y, w,
buttons = [
    [classic, C_button, blue, violet_blue, 200, 600, 100, 50],
    [new, N_button, red, dar_red, 400, 600, 100, 50]
]


def button_hover(button_x, button_w, button_y, button_h, disply, color, rect, text, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button_x + button_w > mouse[0] > button_x and button_y + (button_h / 2) > mouse[1] > button_y:
        pygame.draw.rect(disply, hover_color, rect)
        Display.blit(text, rect)
    else:
        pygame.draw.rect(disply, color, rect)
        Display.blit(text, rect)

    clock.tick(15)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def menu_screen():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        Display.blit(bg, (0, 0))
        Textsuf, Textrect = text_objects("BattleShip", LG_F)
        Textrect.center = (400, 350)
        Display.blit(Textsuf, Textrect)
        for text, rect, color, hover, B_x, B_y, B_w, B_h in buttons:
            button_hover(B_x, B_h, B_y, B_w, Display, color, rect, text, hover)
        pygame.display.update()
        pygame.display.flip()


menu_screen()
pygame.QUIT
