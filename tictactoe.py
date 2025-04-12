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