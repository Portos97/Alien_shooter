import pygame.font


class Button:

    def __init__(self, as_game, message):
        self.screen = as_game.screen
        self.screen_rect = self.screen.get_rect()
        # Button properties
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 42)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_message(message)

    def prep_message(self, message):
        """Text on the button"""
        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        """Display of the button with text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
