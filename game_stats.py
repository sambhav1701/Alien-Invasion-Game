class GameStats:  #Track game statistics
    def __init__(self, ai_game):  #Initialization statistics
        self.game_active = True
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False  # When the game starts, it is inactive
        self.high_score = 0
        

    def reset_stats(self):  #Initializes statistics that may change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        