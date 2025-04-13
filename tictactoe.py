import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)

# Game board
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
game_over = False

# Font
font = pygame.font.Font(None, 120)

def draw_board():
    screen.fill(WHITE)
    # Draw grid lines
    pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), 5)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), 5)
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), 5)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), 5)
    
    # Draw X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                x_pos = col * WIDTH // 3 + WIDTH // 6
                y_pos = row * HEIGHT // 3 + HEIGHT // 6
                text = font.render('X', True, BLACK)
                screen.blit(text, (x_pos - text.get_width() // 2, y_pos - text.get_height() // 2))
            elif board[row][col] == 'O':
                x_pos = col * WIDTH // 3 + WIDTH // 6
                y_pos = row * HEIGHT // 3 + HEIGHT // 6
                text = font.render('O', True, BLACK)
                screen.blit(text, (x_pos - text.get_width() // 2, y_pos - text.get_height() // 2))

def check_winner():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    
    # Check for tie
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        return 'Tie'
    
    return None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // (HEIGHT // 3)
            clicked_col = mouseX // (WIDTH // 3)
            
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = current_player
                
                winner = check_winner()
                if winner:
                    game_over = True
                    if winner == 'Tie':
                        result_text = "It's a Tie!"
                    else:
                        result_text = f"{winner} wins!"
                else:
                    current_player = 'O' if current_player == 'X' else 'X'


        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                # Reset game
                board = [['', '', ''], ['', '', ''], ['', '', '']]
                current_player = 'X'
                game_over = False  

    draw_board()

    if game_over:
        font = pygame.font.Font(None, 50)
        text = font.render(result_text, True, BLACK)
        restart_text = font.render("Press R to restart", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))
        
    pygame.display.flip()