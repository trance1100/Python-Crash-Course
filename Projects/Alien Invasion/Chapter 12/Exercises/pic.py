import pygame

class Rocket():
    
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/stick.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.rocket_speed
        if self.moving_up:
            self.center2 -= self.ai_settings.rocket_speed
        if self.moving_down:
            self.center2 += self.ai_settings.rocket_speed
        
        self.rect.centerx = self.center
        self.rect.centery = self.center2

    def blitme(self):
        self.screen.blit(self.image, self.rect)