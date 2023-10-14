import pygame
from screen import Screen
import database

def show_victory_screen(winner, final_score):
    pygame.font.init()
    screen = Screen()
    window = pygame.display.set_mode((screen.WIDTH, screen.HEIGHT))
    running = True

    input_box = pygame.Rect(screen.WIDTH // 2 - 70, screen.HEIGHT // 2, 140, 32)
    save_button = pygame.Rect(screen.WIDTH // 2 - 40, screen.HEIGHT // 2 + 50, 80, 40)

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                elif save_button.collidepoint(event.pos):
                    print("Save button clicked.")
                    print(f"Winner: {winner}, Score: {final_score}, Username: {text}")
                    database.add_score(winner, text, final_score)
                    running = False
                    return 'GAME_OVER'
                color = color_active if active else color_inactive
                
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)
        window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(window, color, input_box, 2)

        save_surface = font.render("Save", True, (0, 0, 0))
        pygame.draw.rect(window, (0, 255, 0), save_button)
        window.blit(save_surface, (save_button.x + 20, save_button.y + 10))

        winner_text = font.render(winner, True, (255, 255, 255))
        window.blit(winner_text, (screen.WIDTH // 2 - winner_text.get_width() // 2, screen.HEIGHT // 2 - 60))

        pygame.display.flip()
