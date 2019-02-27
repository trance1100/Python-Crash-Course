import pygame, sys

from settings import Settings
from figure import Figure

import game_functions as gf 

def start_game():
    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Blue Sky & Character")

    character = Figure(screen)
    
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, character)

start_game()