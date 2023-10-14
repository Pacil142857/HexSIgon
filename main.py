import pygame
from Board import Board
from HexUI import HexUI
from OrderUI import OrderUI

# Initalize pygame with a screen
pygame.init()
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(width, height)

board = Board()
hexes = []
orders = []
radius = height / 5
center_x = 2 * width // 3
center_y = height // 2

# Add HexUIs
hexes.add(HexUI(board.hexes[0], center_x - 5 * radius // 3, center_y - radius, radius))
hexes.add(HexUI(board.hexes[1], center_x - 5 * radius // 3, center_y + radius, radius))
hexes.add(HexUI(board.hexes[2], center_x, center_y - 2 * radius, radius))
hexes.add(HexUI(board.hexes[3]), center_x, center_y, radius)
hexes.add(HexUI(board.hexes[2], center_x, center_y + 2 * radius, radius))
hexes.add(HexUI(board.hexes[5], center_x + 5 * radius // 3, center_y - radius, radius))
hexes.add(HexUI(board.hexes[6], center_x + 5 * radius // 3, center_y + radius, radius))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill((0, 0, 0))
    
pygame.quit()
exit()