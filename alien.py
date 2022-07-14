import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to describe single alien in the fleet"""
    def __init__(self, as_game):
        super().__init__()
        self.screen = as_game.screen
        self.settings = as_game.settings
        # Load of alien picture
        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def edges_screen_check(self):
        """Return True if alien is on the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
