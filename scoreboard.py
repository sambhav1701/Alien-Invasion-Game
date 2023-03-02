import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:   #Class showing score information
    def __init__(self, ai_game):  #Initialization shows the attributes involved in the score
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (30, 30, 30)  # Font settings to use when displaying score information
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()  # Prepare initial score, level and ship image
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):  #Convert the score into a rendered image
        rounded_score = round(self.stats.score, -1)  # Round to an integral multiple of 10
        score_str = "Current Score: " + "{:,}".format(rounded_score)  # Inserts a comma (thousand separator) into a numeric value when it is converted to a string
        self.score_image = self.font.render(score_str, True, (255, 255, 255), self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()  # The score is displayed in the upper right corner of the screen
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):  #Converts the highest score to the rendered image
        high_score = round(self.stats.high_score, -1)
        high_score_str = "Highest Score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, (255, 255, 255), self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()  # The score is displayed in the top center of the screen
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):  #Score and number of remaining ships are displayed on the screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def check_high_score(self):  #Check to see if a new highest score is born
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, (255, 255, 255), self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()  # Put the rank below the score
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10   

    def prep_ships(self):  #Shows how many ships are left
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


