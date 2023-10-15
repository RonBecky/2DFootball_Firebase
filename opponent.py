import pygame
from ball import Ball
from screen import Screen
from player import Player
from goalkeeper import Goalkeeper
from pitch import Pitch


class Opponent:# Blue player (right)
    def __init__(self, x, y, size, neural_net=None):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 5
        self.color = (0, 0, 255)  # Color blue
        self.direction = None
        self.ball_attached = False
        self.facing_direction = 'a'
        self.neural_net = neural_net
        self.screen = Screen()
        self.pitch= Pitch(self.screen.WIDTH, self.screen.HEIGHT)
        self.ball = Ball(self.screen.WIDTH, self.screen.HEIGHT, 10)
        self.player = Player(203, 240, 20)
        self.goalkeeper1 = Goalkeeper(x=25, y=self.screen.HEIGHT / 2 - self.pitch.GOAL_AREA_HEIGHT / 10, width=20, height=20, color=(255, 0, 0), control='scripted')

    def draw(self, window):# Drawing the square
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
    
    
    # Movement for opponent
    def move(self, keys, screen_width, screen_height, ball_attached=False, ball_size=0):   
        if keys[pygame.K_UP] and self.y - self.speed - (ball_attached * ball_size) >= 0:
            self.y -= self.speed
            self.direction = 'up'
        if keys[pygame.K_DOWN] and self.y + self.speed + self.size + (ball_attached * ball_size) <= screen_height:
            self.y += self.speed
            self.direction = 'down'
        if keys[pygame.K_LEFT] and self.x - self.speed - (ball_attached * ball_size) >= 0:
            self.x -= self.speed
            self.direction = 'left'
        if keys[pygame.K_RIGHT] and self.x + self.speed + self.size + (ball_attached * ball_size) <= screen_width:
            self.x += self.speed
            self.direction = 'right'
    
    # Updating ball position when attached
    def update(self, keys, screen_width, screen_height, ball_attached, ball_radius):
        self.move(keys, screen_width, screen_height, ball_attached, ball_radius)
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:# Up left
            self.facing_direction = 'wa'
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:# Up right
            self.facing_direction = 'wd'
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:# Down Left
            self.facing_direction = 'sa'
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:# Down Right
            self.facing_direction = 'sd'
        elif keys[pygame.K_LEFT]:# Left
            self.facing_direction = 'a'
        elif keys[pygame.K_RIGHT]:# Right
            self.facing_direction = 'd'
        elif keys[pygame.K_UP]:# Up
            self.facing_direction = 'w'
        elif keys[pygame.K_DOWN]:# Down
            self.facing_direction = 's'