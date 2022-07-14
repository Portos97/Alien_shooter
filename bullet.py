import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets shot by spaceship"""

    def __init__(self, as_game):
        super().__init__()
        self.screen = as_game.screen
        self.settings = as_game.settings
        self.color = self.settings.bullet_color
        # Creation of bullet and placing it on the screen
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = as_game.spaceship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet on the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def bullet_draw(self):
        """Bullet display on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
