import pygame, sys

class Rain():
    
    def __init__(self, screen):
        super(Rain, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 3, 1)

        # Store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = (46, 99, 232)
        self.speed_factor = 3

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def game_start():
    pygame.init()
    screen = pygame.display.set_mode((800, 400)) 
    pygame.display.set_caption(" - Rain - ")
    screen.fill((46, 48, 53))
    rain = Rain(screen)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        rain.draw_bullet()
        rain.update()
        pygame.display.flip()

game_start()
    
