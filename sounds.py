import pygame

class SoundManager:# Sound effects
    def __init__(self):
        pygame.mixer.init()
        self.crowd_cheer = pygame.mixer.Sound('static\crowd.wav')
        self.end_whistle = pygame.mixer.Sound('static\end_whistle.wav')
        self.start_whistle = pygame.mixer.Sound('static\start_whistle.wav')

    def play_crowd_cheer(self):
        self.crowd_cheer.play()

    def play_end_sound(self):
        self.end_whistle.play()

    def play_whistle_sound(self):
        self.start_whistle.play()