class GameStats:
    """In-game statistics monitoring"""

    def __init__(self, as_game):
        self.settings = as_game.settings
        self.stats_reset()
        self.game_active = False

    def stats_reset(self):
        """Initialize of statistical data that can change during the game"""
        self.spaceship_left = self.settings.spaceship_lives
