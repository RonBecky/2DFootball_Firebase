# menu.py
import pygame
from pitch import Pitch
import database

class Menu:
    def __init__(self, screen, clock):
        self.menu_running = True
        self.return_to_menu = False
        self.screen = screen
        self.clock = clock
        self.my_font = pygame.font.Font(None, 74)
        self.text_surface = self.my_font.render('2D Football', True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(self.screen.WIDTH // 2, 30))
        self.button_font = pygame.font.Font(None, 50)
        self.play_button_rect = pygame.Rect(400, 200, 200, 50)
        self.champions_button_rect = pygame.Rect(400, 300, 200, 50)
        self.pitch = Pitch(self.screen.WIDTH, self.screen.HEIGHT)

    def draw_button(self, text, rect, color):
        pygame.draw.rect(self.screen.window, color, rect)
        button_text = self.button_font.render(text, True, (0, 0, 0))
        button_rect = button_text.get_rect(center=rect.center)
        self.screen.window.blit(button_text, button_rect)

    def run(self):
        while self.menu_running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.play_button_rect.collidepoint(x, y):
                        print("Play button clicked!")
                        self.menu_running = False
                        return 'play'
                    elif self.champions_button_rect.collidepoint(x, y):
                        print("Champions button clicked!")
                        scores = database.fetch_scores()
                        print(scores)
                        return 'champions'
            

            self.pitch_surface = pygame.Surface((self.screen.WIDTH, self.screen.HEIGHT))
            self.pitch.draw(self.pitch_surface)
            self.screen.window.blit(self.pitch_surface, (0, 0))
            self.screen.window.blit(self.text_surface, self.text_rect)
            self.draw_button("Play", self.play_button_rect, (0, 128, 0))
            self.draw_button("Champions", self.champions_button_rect, (0, 0, 128))
            
            
            
            pygame.display.flip()
        
    def draw_leaderboard(self, scores):
        leaderboard_background = pygame.Surface((self.screen.WIDTH, self.screen.HEIGHT), pygame.SRCALPHA)
        leaderboard_background.fill((0, 0, 0, 128))
        self.screen.window.blit(leaderboard_background, (0, 0))
        
        title_font = pygame.font.Font(None, 74)
        title_text = title_font.render('Leaderboard', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen.WIDTH // 2, 30))
        pygame.draw.rect(self.screen.window, (0, 0, 0),(title_rect.x, title_rect.y, title_rect.width, title_rect.height))
    
        score_font = pygame.font.Font(None, 50)
        start_y = 100  # starting y-coordinate for scores
        offset = 60   # vertical offset between scores
    
        # Drawing the leaderboard title
        self.screen.window.blit(title_text, title_rect)
        
        
        if scores is None or len(scores) == 0:  # Check if scores is None or empty
           none_text = score_font.render("None", True, (255, 255, 255))
           none_rect = none_text.get_rect(center=(self.screen.WIDTH // 2, start_y))
           self.screen.window.blit(none_text, none_rect)
        else:
            for idx, (key, score) in enumerate(scores.items()):
                score_str = f"{score['username']} ({score['winner']}) - {score['final_score']}"
                score_text = score_font.render(score_str, True, (255, 255, 255))
                score_rect = score_text.get_rect(center=(self.screen.WIDTH // 2, start_y + idx * offset))
                self.screen.window.blit(score_text, score_rect)
    
        pygame.display.flip()
