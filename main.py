import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from spaceship import Spaceship
from alien import Alien
from bullet import Bullet
from start_button import Button


class Aliengame:
    """Generic class to manage resources and how the game works"""

    def __init__(self):
        """Game starter"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Game")

        self.stats = GameStats(self)
        self.spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_alien_fleet()
        self.play_button = Button(self, "Play")

    def game_run(self):
        """Start of the main iteration"""
        run = True
        while run:
            self.events_check()

            if self.stats.game_active:
                self.spaceship.update()
                self.projectile_update()
                self.alien_update()

            self.screen_update()

    def events_check(self):
        """Respond to keyboard and mouse interaction"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_key_push(event)
            elif event.type == pygame.KEYUP:
                self.check_key_release(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self.check_play_button(mouse_position)

    def check_play_button(self, mouse_position):
        """Start of the game with play button"""
        button_click = self.play_button.rect.collidepoint(mouse_position)
        if button_click and not self.stats.game_active:
            self.stats.stats_reset()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self.create_alien_fleet()
            self.spaceship.spaceship_centre()
            pygame.mouse.set_visible(False)

    def check_key_push(self, event):
        """Reaction to pressing a key"""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bullet_fire()

    def check_key_release(self, event):
        """Reaction to key release"""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False

    def bullet_fire(self):
        """Creation of the new bullet"""
        if len(self.bullets) < self.settings.bullets_allowed_scr:
            new_bullets = Bullet(self)
            self.bullets.add(new_bullets)

    def projectile_update(self):
        """Projectile position update and removing that off-screen ones"""
        self.bullets.update()
        # Deleting bullets that are off-screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.check_missile_alien_collision()

    def check_missile_alien_collision(self):
        """Check if missile hit the target"""
        bullet_contact = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self.create_alien_fleet()

    def alien_update(self):
        """Alien position update and check if the alien fleet is on the edge of the screen"""
        self.check_fleet_edges()
        self.aliens.update()

        # Detection of collisions between alien and spaceship
        if pygame.sprite.spritecollideany(self.spaceship, self.aliens):
            self.spaceship_hit()
        self.alien_hit_bottom()

    def create_alien_fleet(self):
        """Creation of fleet of the aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        space_on_the_screen = self.settings.screen_width - (2 * alien_width)
        number_of_aliens = space_on_the_screen // (2 * alien_width)

        # Number of alien rows on the screen
        spaceship_height = self.spaceship.rect.height
        available_space = (self.settings.screen_height - (3 * alien_height) - spaceship_height)
        rows_number = available_space // (2 * alien_height)

        # Creation of first line of aliens
        for row_number in range(rows_number):
            for alien_number in range(number_of_aliens):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        """"Creation of alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def check_fleet_edges(self):
        """Reaction of alien moving to the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.edges_screen_check():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Move the fleet to the bottom of the screen"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_speed_drop
        self.settings.fleet_direction *= -1

    def spaceship_hit(self):
        """Reaction to an alien hitting the ship"""
        if self.stats.spaceship_left > 0:
            self.stats.spaceship_left = -1
            self.aliens.empty()
            self.bullets.empty()
            self.create_alien_fleet()
            self.spaceship.spaceship_centre()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def alien_hit_bottom(self):
        """Check if alien hit the bottom edge"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.spaceship_hit()
                break

    def screen_update(self):
        """Screen updates"""
        self.screen.fill(self.settings.background_color)
        self.spaceship.ship_blit()
        for bullet in self.bullets.sprites():
            bullet.bullet_draw()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # To run the game
    ag = Aliengame()
    ag.game_run()
