import pygame
from goalkeeper import Goalkeeper
from pitch import Pitch
from player import Player
from opponent import Opponent
from ball import Ball
from score import Score
from screen import Screen
from func import actions
from victoryScreen import show_victory_screen




#GameLoop = the main game loop in a class
class GameLoop:
    
    pygame.display.set_caption("2D Football")
    def __init__(self, screen, clock):
        self.running = True
        self.clock = clock
        self.screen = screen
        self.window = pygame.display.set_mode((self.screen.WIDTH, self.screen.HEIGHT))
        self.pitch = Pitch(self.screen.WIDTH, self.screen.HEIGHT)
        self.goalkeeper1 = Goalkeeper(x=25, y=self.screen.HEIGHT / 2 - self.pitch.GOAL_AREA_HEIGHT / 10, width=20, height=20, color=(255, 0, 0), control='scripted')
        self.goalkeeper2 = Goalkeeper(x=self.screen.WIDTH - self.pitch.GOAL_AREA_WIDTH + 13, y=self.screen.HEIGHT / 2 - self.pitch.GOAL_AREA_HEIGHT / 10, width=20, height=20, color=(0, 0, 255), control='scripted')
        self.player = Player(203, 240, 20)
        self.keys = pygame.key.get_pressed()
        self.opponent_keys = pygame.key.get_pressed()
        self.opponent = Opponent(self.screen.WIDTH - 223, 240, 20)
        self.ball = Ball(self.screen.WIDTH, self.screen.HEIGHT, 10)
        self.score = Score(self.screen.WIDTH, self.screen.HEIGHT)
        self.Func = actions()
        
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.keys = pygame.key.get_pressed()
            self.opponent_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:# Setting the X on the window as a quit button
                   self.running = False
            
            
            # Update the player's position and other related properties
            # Parameters: keys pressed, screen width, screen height, whether the ball is attached to the player, and the ball radius.
            self.player.update(self.keys, self.screen.WIDTH, self.screen.HEIGHT, self.player.ball_attached, self.ball.radius)
            self.opponent.update(self.opponent_keys, self.screen.WIDTH, self.screen.HEIGHT, self.opponent.ball_attached, self.ball.radius)# For opponent
            
            # Check if the ball should be attached to either the player or opponent, if not already attached.
            if not self.player.ball_attached or not self.opponent.ball_attached:
                self.Func.check_and_attach_ball(self.player, self.opponent, self.ball)
            
            # Handle the ball's attachment logic for both player and opponent.
            self.Func.handle_ball_attachment(self.player, self.opponent, self.ball)
            
            # Handle the shooting mechanism for the player.
            # Parameters: player's keys, the player's current facing direction, and whether the ball is attached to the player or opponent.
            player_angle, player_ball_speed_x, player_ball_speed_y, player_shoot_delay, self.player.ball_attached = self.Func.handle_shooting(
                self.keys[pygame.K_SPACE], pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, self.player.ball_attached, self.player.facing_direction, self.opponent.ball_attached)
            # For opponent
            opponent_angle, opponent_ball_speed_x, opponent_ball_speed_y, opponent_shoot_delay, self.opponent.ball_attached = self.Func.handle_shooting(
                self.keys[pygame.K_KP0], pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, self.opponent.ball_attached, self.opponent.facing_direction, self.player.ball_attached)
            
            
            self.Func.handle_shooting_logic(self.player, player_angle, player_ball_speed_x, player_ball_speed_y, player_shoot_delay) # Apply the shooting logic (e.g., set speed and direction) for the player.
            self.Func.handle_shooting_logic(self.opponent, opponent_angle, opponent_ball_speed_x, opponent_ball_speed_y, opponent_shoot_delay)# Apply the shooting logic for the opponent.
            self.Func.update_ball_position(self)# Update the ball's position based on its speed and handle any collisions.
            self.Func.manage_shoot_delay(self)# Manage the shoot delay, decrementing it as time progresses.
            self.Func.check_goals_and_reset(self)# Check if a goal has been scored and reset positions if necessary.
            self.Func.handle_goalkeeper_collision(self)# Handle any collision between the ball and the goalkeepers.
            
            goal_area_top = self.pitch.screen_height / 2 - self.pitch.GOAL_AREA_HEIGHT / 2
            goal_area_bottom = self.pitch.screen_height / 2 + self.pitch.GOAL_AREA_HEIGHT / 2
            self.goalkeeper1.move(goal_area_top, goal_area_bottom)
            self.goalkeeper2.move(goal_area_top, goal_area_bottom)
            
        
        
            # Drawing everything on screen
            self.pitch_surface = pygame.Surface((self.screen.WIDTH, self.screen.HEIGHT))
            self.pitch.draw(self.pitch_surface)
            self.player.draw(self.pitch_surface)
            self.opponent.draw(self.pitch_surface)
            self.ball.draw(self.pitch_surface)
            self.score.draw(self.pitch_surface)
            self.goalkeeper1.draw(self.pitch_surface)
            self.goalkeeper2.draw(self.pitch_surface)
            self.window.blit(self.pitch_surface, (0, 0))
            
            pygame.display.flip()
            
            game_over_info = self.Func.check_game_over(self)
        #     if game_over_info:  # If a tuple is returned, then game_over_info will be non-None.
        #         action, winner, final_score = game_over_info  # Unpack the returned tuple
        #     #     # if action == "GAME_OVER":
        #     #     #     show_victory_screen(winner, final_score)  # Show victory screen here, assuming it exits immediately after showing
        #     #     # self.running = False  # This line will stop the main game loop
            
        return game_over_info
        
        
    