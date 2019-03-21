import sys
import pygame

def main():
    pygame.pygame.init()

    logo = pygame.pygame.image.load("godofwar.png")
    pygame.pygame.dispay.pygame.display.set_icon(logo)
    pygame.dispay.pygame.display.set_caption("first run", icontitle=None)

    screen = pygame.dispay.set_mode(240,180)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.pygame.QUIT:
                running = false

if __name__ == "__main__":
    main()