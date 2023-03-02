
class Settings:  #Storage game "alien invasion" in all settings of the class

    def __init__(self):  #Initialize the static settings of the game
        self.screen_width = 1200  # screen setting
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1.5
        self.bullet_speed = 1.5   # Bullet setting
        self.bullet_width = 3  
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3  # Maximum bullets
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10  # The speed of moving down the line
        self.speedup_scale = 1.1  # Speed up the game
        self.score_scale = 1.5  # The speed of alien score increase
        self.initialize_dynamic_settings()
        self.fleet_direction = 1
        self.ship_limit = 3  # Total number of ships available

    def initialize_dynamic_settings(self):  #Initializes settings that change as the game progresses
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1  # 1 means to move to the right, - 1 means to move to the left
        self.alien_points = 50  # An alien scored

    def increase_speed(self):  #Increase speed setting and alien score
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

