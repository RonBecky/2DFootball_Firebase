import pygame
from sounds import SoundManager

class Score:# Drawing the scores
    def __init__(self, screen_width, screen_height, font_size=32):
        self.score_home = 0
        self.score_away = 0
        self.sounds = SoundManager()
        self.font = pygame.font.Font(None, font_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (0, 0, 0) 

    def increase_home(self):# Increase home score
        self.score_home += 1
        self.sounds.play_crowd_cheer()# Play sound when score increased
    
    def increase_away(self):# Increase away score
        self.score_away += 1
        self.sounds.play_crowd_cheer()# Play sound when score increased

    def draw(self, surface):# Drawing score
        score_text = f"{self.score_home}:{self.score_away}"
        text = self.font.render(score_text, True, self.color)
        x = (self.screen_width - text.get_width()) // 2
        y = 10
        surface.blit(text, (x, y))

