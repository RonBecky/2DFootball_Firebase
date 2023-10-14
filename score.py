import pygame

class Score:
    def __init__(self, screen_width, screen_height, font_size=32):
        self.score_home = 0
        self.score_away = 0
        pygame.font.init()
        self.font = pygame.font.Font(None, font_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (0, 0, 0) 

    def increase_home(self):
        self.score_home += 1

    def increase_away(self):
        self.score_away += 1

    def draw(self, surface):
        score_text = f"{self.score_home}:{self.score_away}"
        text = self.font.render(score_text, True, self.color)
        x = (self.screen_width - text.get_width()) // 2
        y = 10
        surface.blit(text, (x, y))

