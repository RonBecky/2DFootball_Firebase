import pygame

class Ball:
    def __init__(self, screen_width, screen_height, radius):
        self.x = screen_width // 2 # x ball positioning
        self.y = screen_height // 2# y ball positioning
        self.radius = radius# How big the ball is
        self.color = (255, 255, 0)# The color of the ball (yellow)
        self.goal_scored = False# Cheking if the ball touched the net 
        self.speed_x = 0# Ball's x speed
        self.speed_y = 0# Ball's y speed
        self.shoot_delay = 0# Ball's cooldown after being shot

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)# Drawing the ball