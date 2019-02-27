import pygame, sys

def start_game():
    pygame.init()
    bg_color = (98, 182, 234)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()

start_game()