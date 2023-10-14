import pygame
from screen import Screen
from menu import Menu
from gameLoop import GameLoop
import database
from victoryScreen import show_victory_screen

def main():
    pygame.init()
    pygame.display.set_caption("2D Football")
    
    screen = Screen()
    clock = pygame.time.Clock()
    
    menu = Menu(screen, clock)
    
    while True:
        print("Inside main loop")
        action = menu.run()
        print(f"Action from menu: {action}")
        if action == 'play':
            game_loop = GameLoop(screen, clock)
            print("Inside game loop")
            while game_loop.running:
                game_over_info = game_loop.run()
                print(f"Game over info: {game_over_info}")
                if game_over_info:
                    action = game_over_info
                    print(f"Action from show_victory_screen: {action}")
                    if action == 'quit':
                        pygame.quit()
                        return  # Exit the main function
                    if action == 'GAME_OVER':
                        print("Breaking out to menu.")
                        game_loop.running = False
                    menu.menu_running= True
        elif action == 'champions':
            scores = database.fetch_scores()
            menu.draw_leaderboard(scores)
            pygame.time.wait(5000)
        else:
            pygame.quit()
            break


if __name__ == '__main__':
    main()
