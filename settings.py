class Settings:
    """Settings of the game"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.background_color = (255, 255, 255)
        # Spaceship settings
        self.spaceship_speed = 0.7
        self.spaceship_lives = 3
        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed_scr = 3
        # Alien settings
        self.alien_speed = 1
        self.fleet_speed_drop = 10
        self.fleet_direction = 1
