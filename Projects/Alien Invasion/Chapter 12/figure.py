import pygame

class Figure():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/stick.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
