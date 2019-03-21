import pygame

black = 0, 0, 0
blue = 0, 0, 128
red = 255, 0, 0
green = 0, 100, 0


def text_objects(text, font):
    textsurface = font.render(text, True, blue)
    return textsurface, textsurface.get_rect()


pygame.init()
running = True

size = width, height = (700, 500)
rect1 = pygame


fonte = pygame.font.get_default_font()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()

    if mouse

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Battle Ship")
    screen.fill(black)
    largeText = pygame.font.Font(fonte, 115)
    TextSurf, TextRect = text_objects("BattleShip", largeText)
    TextRect.center = (350, 250)
    pygame.draw.rect(screen, green, (150, 400, 100, 70))
    pygame.draw.rect(screen, red, (550, 400, 100, 70))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    pygame.display.flip()

