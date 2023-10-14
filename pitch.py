import pygame

class Pitch:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height 
        self.GOAL_AREA_WIDTH = 60
        self.GOAL_AREA_HEIGHT = 100
        self.GOAL_WIDTH = 10
        self.GOAL_HEIGHT = 100
        self.SHADING_WIDTH = 10
        

    def draw(self, pitch):
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        
        # Fill the pitch with green color
        pitch.fill(GREEN)
        
        # Draw outer boundary lines
        pygame.draw.line(pitch, WHITE, (0, 0), (0, self.screen_height), 5)
        pygame.draw.line(pitch, WHITE, (0, self.screen_height), (self.screen_width, self.screen_height), 5)
        pygame.draw.line(pitch, WHITE, (self.screen_width, self.screen_height), (self.screen_width, 0), 5)
        pygame.draw.line(pitch, WHITE, (self.screen_width, 0), (0, 0), 5)

        # Draw halfway line
        pygame.draw.line(pitch, WHITE, (self.screen_width / 2, 0), (self.screen_width / 2, self.screen_height), 5)

        # Draw center circle
        pygame.draw.circle(pitch, WHITE, (self.screen_width / 2, self.screen_height / 2), 60, 5)

        # Draw big goal area left
        pygame.draw.line(pitch, WHITE, (0, self.screen_height / 5), (self.screen_width / 5, self.screen_height / 5), 5)
        pygame.draw.line(pitch, WHITE, (self.screen_width / 5, self.screen_height / 5), (self.screen_width / 5, self.screen_height / 5 * 4), 5)
        pygame.draw.line(pitch, WHITE, (self.screen_width / 5, self.screen_height / 5 * 4), (0, self.screen_height / 5 * 4), 5)

        # Draw big goal area right
        pygame.draw.line(pitch, WHITE, (self.screen_width, self.screen_height / 5), (self.screen_width * 4 / 5, self.screen_height / 5), 5)
        pygame.draw.line(pitch, WHITE, (self.screen_width * 4 / 5, self.screen_height / 5), (self.screen_width * 4 / 5, self.screen_height / 5 * 4), 5)
        pygame.draw.line(pitch, WHITE, (self.screen_width * 4 / 5, self.screen_height / 5 * 4), (self.screen_width, self.screen_height / 5 * 4), 5)

        # Draw small goal area left and right
        pygame.draw.rect(pitch, WHITE, (0, self.screen_height / 2 - self.GOAL_AREA_HEIGHT / 2, self.GOAL_AREA_WIDTH, self.GOAL_AREA_HEIGHT), 2)
        pygame.draw.rect(pitch, WHITE, (self.screen_width - self.GOAL_AREA_WIDTH, self.screen_height / 2 - self.GOAL_AREA_HEIGHT / 2, self.GOAL_AREA_WIDTH, self.GOAL_AREA_HEIGHT), 2)

        # Draw goal posts and shading
        pygame.draw.rect(pitch, WHITE, (0, self.screen_height / 2 - self.GOAL_HEIGHT / 2, self.GOAL_WIDTH, self.GOAL_HEIGHT))
        pygame.draw.rect(pitch, (200, 200, 200), (self.GOAL_WIDTH, self.screen_height / 2 - self.GOAL_HEIGHT / 2, self.SHADING_WIDTH, self.GOAL_HEIGHT))
        pygame.draw.rect(pitch, WHITE, (self.screen_width - self.GOAL_WIDTH, self.screen_height / 2 - self.GOAL_HEIGHT / 2, self.GOAL_WIDTH, self.GOAL_HEIGHT))
        pygame.draw.rect(pitch, (200, 200, 200), (self.screen_width - self.GOAL_WIDTH - self.SHADING_WIDTH, self.screen_height / 2 - self.GOAL_HEIGHT / 2, self.SHADING_WIDTH, self.GOAL_HEIGHT))
