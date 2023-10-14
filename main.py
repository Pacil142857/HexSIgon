import pygame
from Board import Board
from HexUI import HexUI
from OrderUI import OrderUI

from Order import Order
from Hex import Hex

# Initalize pygame with a screen
pygame.init()
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))

board = Board()
hexes = []
orders = []
radius = height / 6
center_x = 2 * width // 3
center_y = height // 2

# Add HexUIs
hexes.append(HexUI(board.hexes[0], center_x - 5 * radius // 3, center_y - radius, radius))
hexes.append(HexUI(board.hexes[1], center_x - 5 * radius // 3, center_y + radius, radius))
hexes.append(HexUI(board.hexes[2], center_x, center_y - 2 * radius, radius))
hexes.append(HexUI(board.hexes[3], center_x, center_y, radius))
hexes.append(HexUI(board.hexes[2], center_x, center_y + 2 * radius, radius))
hexes.append(HexUI(board.hexes[5], center_x + 5 * radius // 3, center_y - radius, radius))
hexes.append(HexUI(board.hexes[6], center_x + 5 * radius // 3, center_y + radius, radius))

# Add OrderUIs
orders.append(OrderUI(board.orders[0], 20, 20))
orders.append(OrderUI(board.orders[1], 20, 20 + height // 3))
orders.append(OrderUI(board.orders[2], 20, 20 + 2 * height // 3))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill((0, 0, 0))
    for hex in hexes:
        hex.draw(screen)
    for order in orders:
        order.draw(screen)
    pygame.display.flip()
    
pygame.quit()
exit()
