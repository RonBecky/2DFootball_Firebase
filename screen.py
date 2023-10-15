import pygame

class Screen:# Setting the screen and window for all other components
    def __init__(self):
       # Constants for screen size
       self.WIDTH = 1000
       self.HEIGHT = 500
       self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))