import pygame
from screen import Screen
from menu import Menu
from gameLoop import GameLoop
import database
from sounds import SoundManager

def main():# The loop that decides the order of the loops
    pygame.init()
    pygame.display.set_caption("2D Football")
    
    screen = Screen()
    clock = pygame.time.Clock()
    sounds = SoundManager()
    menu = Menu(screen, clock)
    
    while True:
        # print("Inside main loop")
        action = menu.run()
        # print(f"Action from menu: {action}")
        if action == 'play':# Starting the game loop
            game_loop = GameLoop(screen, clock)
            sounds.play_whistle_sound()
            # print("Inside game loop")
            while game_loop.running:
                game_over_info = game_loop.run()
                # print(f"Game over info: {game_over_info}")
                if game_over_info:
                    action = game_over_info
                    # print(f"Action from show_victory_screen: {action}")
                    if action == 'quit':
                        pygame.quit()
                        return  # Exit the main function
                    if action == 'GAME_OVER':
                        # print("Breaking out to menu.")
                        game_loop.running = False
                    menu.menu_running= True
        elif action == 'champions':# Showing the leaderboard
            scores = database.fetch_scores()
            menu.draw_leaderboard(scores)
            pygame.time.wait(5000)
        else:
            pygame.quit()
            break


if __name__ == '__main__':
    main()
