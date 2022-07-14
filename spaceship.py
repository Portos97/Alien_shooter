import pygame


class Spaceship:
    """Class to manage spaceship"""

    def __init__(self, as_game):
        self.screen = as_game.screen
        self.settings = as_game.settings
        self.screen_rect = as_game.screen.get_rect()
        # Load of battleship picture
        self.image = pygame.image.load('assets/spaceship_red.png')
        self.image_scale = pygame.transform.rotate(pygame.transform.scale(self.image, (65, 45)), 180)
        self.rect = self.image_scale.get_rect()
        self.spaceship_centre()
        # Options to move spaceship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update of location of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed
        # update of rect through the self.x value
        self.rect.x = self.x

    def ship_blit(self):
        self.screen.blit(self.image_scale, self.rect)

    def spaceship_centre(self):
        """Placing spaceship in the middle at the bottom edge"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
