import math
import pygame
from pitch import Pitch
from player import Player
from opponent import Opponent
from ball import Ball
from score import Score
from screen import Screen
from victoryScreen import show_victory_screen
from sounds import SoundManager




class actions():
    def __init__(self):
        self.screen = Screen()
        self.pitch = Pitch(self.screen.WIDTH, self.screen.HEIGHT)
        self.player = Player(203, 240, 20)
        self.opponent = Opponent(self.screen.WIDTH - 223, 240, 20)
        self.ball = Ball(self.screen.WIDTH, self.screen.HEIGHT, 10)
        self.score = Score(self.screen.WIDTH, self.screen.HEIGHT)
        self.sounds = SoundManager()
        
        
    def is_close_to_ball(self, player, ball):
        return ((player.x - ball.x) ** 2 + (player.y - ball.y) ** 2) ** 0.5 < player.size + ball.radius# Cheking the distance bitween the ball and the entity
    
    def is_colliding_with_goalkeeper(self, goalkeeper, ball):
        distance = math.sqrt((goalkeeper.x - ball.x)**2 + (goalkeeper.y - ball.y)**2)# Cheking if the ball has touched the keeper
        return distance < goalkeeper.width / 2 + ball.radius# If the ball has touched the keeper the ball wil get deflected
    
    # Ball attachments for entitys
    def attach_ball_to_entity(self, entity, ball, facing_direction):# Responsible for attaching the ball to a particular position around the entity based on which direction the entity is facing.
        offset = 10
        if facing_direction == 'w':
            ball.x, ball.y = entity.x + entity.size // 2, entity.y - offset
        elif facing_direction == 's':
            ball.x, ball.y = entity.x + entity.size // 2, entity.y + entity.size + offset
        elif facing_direction == 'a':
            ball.x, ball.y = entity.x - offset, entity.y + entity.size // 2
        elif facing_direction == 'd':
            ball.x, ball.y = entity.x + entity.size + offset, entity.y + entity.size // 2
        elif facing_direction == 'wa':
            ball.x = entity.x - ball.radius
            ball.y = entity.y - ball.radius
        elif facing_direction == 'wd':
            ball.x = entity.x + entity.size + ball.radius
            ball.y = entity.y - ball.radius
        elif facing_direction == 'sa':
            ball.x = entity.x - ball.radius
            ball.y = entity.y + entity.size + ball.radius
        elif facing_direction == 'sd':
            ball.x = entity.x + entity.size + ball.radius
            ball.y = entity.y + entity.size + ball.radius
    
    def check_and_attach_ball(self, player, opponent, ball):# Responsible for attaching the ball to an entity
        if not player.ball_attached and not opponent.ball_attached:
            if self.is_close_to_ball(player, ball) and ball.shoot_delay == 0:
                player.ball_attached = True
                self.attach_ball_to_entity(player, ball, player.facing_direction)
            elif self.is_close_to_ball(opponent, ball) and ball.shoot_delay == 0:
                opponent.ball_attached = True
                self.attach_ball_to_entity(opponent, ball, opponent.facing_direction)
    
    # Resets positions for entitys and ball
    def reset_positions(self, player, opponent, ball, screen):# Resets the position of everything on the pitch after a goal was scored
        player.x, player.y = 203, 240
        opponent.x, opponent.y = screen.WIDTH - 223, 240  # Reset opponent's position
        ball.x, ball.y = screen.WIDTH / 2, screen.HEIGHT / 2
        ball.speed_x = 0
        ball.speed_y = 0
        ball.shoot_delay = 0
        ball.goal_scored = False  # Reset the goal_scored flag here
        player.ball_attached = False  # Detaching the ball from the player
        opponent.ball_attached = False  # Detaching the ball from the opponent
    
    def handle_ball_attachment(self, player, opponent, ball):# Responsible for ball stealing
        if player.ball_attached:
            self.attach_ball_to_entity(player, ball, player.facing_direction)
            if self.is_close_to_ball(opponent, ball) and ball.shoot_delay == 0:
                opponent.ball_attached = True
                player.ball_attached = False
                self.attach_ball_to_entity(opponent, ball, opponent.facing_direction)
        elif opponent.ball_attached:
            self.attach_ball_to_entity(opponent, ball, opponent.facing_direction)
            if self.is_close_to_ball(player, ball) and ball.shoot_delay == 0:
                player.ball_attached = True
                opponent.ball_attached = False
                self.attach_ball_to_entity(player, ball, player.facing_direction)
            
    
    # Shooting angles and behavior
    def handle_shooting(self, shoot_key_pressed, key_up, key_down, key_left, key_right, attached, facing_direction, opponent_attached):# Handles the ball movement while in "shot" state, the angle and speed
        keys = pygame.key.get_pressed()
        
        if shoot_key_pressed and attached and self.ball.shoot_delay == 0:# While moving aka a movement key is pressed
            direction_chosen = False
    
            if keys[key_up] and keys[key_right]:
                angle = math.radians(45)
                direction_chosen = True
            elif keys[key_up] and keys[key_left]:
                angle = math.radians(135)
                direction_chosen = True
            elif keys[key_down] and keys[key_right]:
                angle = math.radians(-45)
                direction_chosen = True
            elif keys[key_down] and keys[key_left]:
                angle = math.radians(-135)
                direction_chosen = True
            elif keys[key_up]:
                angle = math.radians(90)
                direction_chosen = True
            elif keys[key_down]:
                angle = math.radians(-90)
                direction_chosen = True
            elif keys[key_left]:
                angle = math.radians(180)
                direction_chosen = True
            elif keys[key_right]:
                angle = math.radians(0)
                direction_chosen = True
    
            if not direction_chosen and facing_direction:# While standing still aka not pressing any key
                if facing_direction == 'w':
                    angle = math.radians(90)
                elif facing_direction == 's':
                    angle = math.radians(-90)
                elif facing_direction == 'a':
                    angle = math.radians(180)
                elif facing_direction == 'd':
                    angle = math.radians(0)
    
            return angle, 15 * math.cos(angle), 15 * -math.sin(angle), 15, False
        else:
            return None, 0, 0, 0, attached
    
    def handle_shooting_logic(self, entity, angle, speed_x, speed_y, shoot_delay):
        if angle is not None:
            self.ball.speed_x = speed_x
            self.ball.speed_y = speed_y
            self.ball.shoot_delay = shoot_delay
            entity.ball_attached = False
    
    def update_ball_position(self, game_instance):# Updating the ball position on the pitch every time
        self.ball = game_instance.ball
        self.screen = game_instance.screen
        
        # Update ball position based on its current speed
        if self.ball.speed_x != 0 or self.ball.speed_y != 0:
            self.ball.x += self.ball.speed_x
            self.ball.y += self.ball.speed_y

            # Check for collisions with screen bounds
            if self.ball.y - self.ball.radius <= 0 or self.ball.y + self.ball.radius >= self.screen.HEIGHT:
                self.ball.speed_y = -self.ball.speed_y

            if self.ball.x - self.ball.radius <= 0 or self.ball.x + self.ball.radius >= self.screen.WIDTH:
                self.ball.speed_x = -self.ball.speed_x

            # Apply friction
            self.ball.speed_x *= 0.98
            self.ball.speed_y *= 0.98

            # Stop self.ball if speed falls below a certain threshold
            if abs(self.ball.speed_x) < 0.1 and abs(self.ball.speed_y) < 0.1:
                self.ball.speed_x = 0
                self.ball.speed_y = 0
                self.ball.shoot_delay = 0

    
    def manage_shoot_delay(self, game_instance):# Shoot delay for the ball to be able to get shoot and not get stuck to entity
        self.ball = game_instance.ball

        # Decrease the shoot delay counter (if it's greater than 0)
        if self.ball.shoot_delay > 0:
            self.ball.shoot_delay -= 1
            
    def check_goals_and_reset(self, game_instance):# Checking if a goal was made
        ball = game_instance.ball
        pitch = game_instance.pitch
        score = game_instance.score
        screen = game_instance.screen
        
        # Cheking if the goal was scored on the left goal post
        if ball.x - ball.radius <= pitch.GOAL_WIDTH and pitch.screen_height / 2 - pitch.GOAL_HEIGHT / 2 < ball.y < pitch.screen_height / 2 + pitch.GOAL_HEIGHT / 2:
            score.increase_away()
            ball.goal_scored = True
            self.reset_positions(game_instance.player, game_instance.opponent, ball, screen)
        
        # Cheking if the goal was scored on the right goal post
        if ball.x + ball.radius >= pitch.screen_width - pitch.GOAL_WIDTH and pitch.screen_height / 2 - pitch.GOAL_HEIGHT / 2 < ball.y < pitch.screen_height / 2 + pitch.GOAL_HEIGHT / 2:
            score.increase_home()
            ball.goal_scored = True
            self.reset_positions(game_instance.player, game_instance.opponent, ball, screen)
    
    
    def check_game_over(self, game_instance):# Checking if a side scored 5 goals and ending the game
        if game_instance.score.score_home == 5 or game_instance.score.score_away == 5:
            final_score = f"{game_instance.score.score_home}-{game_instance.score.score_away}"  # Get the score before last goal
            if game_instance.score.score_home == 5:
                winner = "Home Won!"
                game_instance.score.increase_home()  # Manually update the score
            elif game_instance.score.score_away == 5:
                winner = "Away Won!"
                game_instance.score.increase_away()  # Manually update the score
    
            show_victory_screen(winner, final_score)  # Pass the final score
            game_instance.running = False
            self.sounds.play_end_sound()
            return "GAME_OVER", winner, final_score
        
    
    def handle_goalkeeper_collision(self, game_instance):# Making the ball to bounce when hitting the goalkeepers
        goalkeeper1 = game_instance.goalkeeper1
        goalkeeper2 = game_instance.goalkeeper2
        ball = game_instance.ball

        if self.is_colliding_with_goalkeeper(goalkeeper1, ball) or self.is_colliding_with_goalkeeper(goalkeeper2, ball):
            ball.speed_x = -ball.speed_x
            ball.speed_y = -ball.speed_y