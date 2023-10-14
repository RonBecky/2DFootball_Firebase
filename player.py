import pygame

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 5
        self.color = (255, 0, 0)
        self.direction = None
        self.ball_attached = False
        self.facing_direction = 'd'

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

    def move(self, keys, screen_width, screen_height, ball_attached=False, ball_size=0):
        if keys[pygame.K_w] and self.y - self.speed - (ball_attached * ball_size) >= 0:
            self.y -= self.speed
            self.direction = 'up'
        if keys[pygame.K_s] and self.y + self.speed + self.size + (ball_attached * ball_size) <= screen_height:
            self.y += self.speed
            self.direction = 'down'
        if keys[pygame.K_a] and self.x - self.speed - (ball_attached * ball_size) >= 0:
            self.x -= self.speed
            self.direction = 'left'
        if keys[pygame.K_d] and self.x + self.speed + self.size + (ball_attached * ball_size) <= screen_width:
            self.x += self.speed
            self.direction = 'right'
    
    def update(self, keys, screen_width, screen_height, ball_attached, ball_radius):
        self.move(keys, screen_width, screen_height, ball_attached, ball_radius)
        if keys[pygame.K_w] and keys[pygame.K_a]:# Up left
            self.facing_direction = 'wa'
        elif keys[pygame.K_w] and keys[pygame.K_d]:# Up right
            self.facing_direction = 'wd'
        elif keys[pygame.K_s] and keys[pygame.K_a]:# Down Left
            self.facing_direction = 'sa'
        elif keys[pygame.K_s] and keys[pygame.K_d]:# Down Right
            self.facing_direction = 'sd'
        elif keys[pygame.K_a]:# Left
            self.facing_direction = 'a'
        elif keys[pygame.K_d]:# Right
            self.facing_direction = 'd'
        elif keys[pygame.K_w]:# Up
            self.facing_direction = 'w'
        elif keys[pygame.K_s]:# Down
            self.facing_direction = 's'
    
        