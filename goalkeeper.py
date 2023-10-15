import pygame

class Goalkeeper:
    def __init__(self, x, y, width, height, color, control='scripted'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 5  # adding speed attribute for movement
        self.control = control  # 'scripted', 'ai', or maybe 'player' for human control
        self.direction = 'up'  # only used in 'scripted'
        self.pause_time = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    

    def move(self, goal_area_top, goal_area_bottom, pause_frames=30):# Setting the movement of the goalkeeper, ai or scripted (no ai right now)
        if self.control == 'scripted':
            self._move_scripted(goal_area_top, goal_area_bottom, pause_frames)
        elif self.control == 'ai':
            self._move_ai(goal_area_top, goal_area_bottom)
        # possibly add more control types here

    def _move_scripted(self, goal_area_top, goal_area_bottom, pause_frames):# Scripted movement
        if self.pause_time > 0:
            self.pause_time -= 1
            return

        if self.direction == 'up':
            self.y = max(goal_area_top, self.y - self.speed)
        elif self.direction == 'down':
            self.y = min(goal_area_bottom - self.height, self.y + self.speed)  # subtract height to make sure the entire object stays within the area

        
        # Inside your move methods (both _move_scripted and _move_ai), after updating self.x or self.y
        self.rect.topleft = (self.x, self.y)
 

        if self.y <= goal_area_top:
            self.direction = 'down'
            self.pause_time = pause_frames
        elif self.y >= goal_area_bottom - self.height:
            self.direction = 'up'
            self.pause_time = pause_frames
        elif self.y == (goal_area_top + goal_area_bottom) / 2:
            self.pause_time = pause_frames

    def _move_ai(self, goal_area_top, goal_area_bottom):# Ai :-:
        # AI logic here
        pass
    