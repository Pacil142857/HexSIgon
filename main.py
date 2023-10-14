import pygame
from Board import Board
from HexUI import HexUI
from OrderUI import OrderUI

from Hex import Hex
from Order import Order

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
board.hexes = [Hex(1), Hex(0, 1), Hex(0, 0, 1), Hex(0, 0, 0, 1), Hex(kelvin = 1), Hex(mole = 1), Hex()]
hexes.append(HexUI(board.hexes[0], center_x - 5 * radius // 3, center_y - radius, radius))
hexes.append(HexUI(board.hexes[1], center_x - 5 * radius // 3, center_y + radius, radius))
hexes.append(HexUI(board.hexes[2], center_x, center_y - 2 * radius, radius))
hexes.append(HexUI(board.hexes[3], center_x, center_y, radius))
hexes.append(HexUI(board.hexes[4], center_x, center_y + 2 * radius, radius))
hexes.append(HexUI(board.hexes[5], center_x + 5 * radius // 3, center_y - radius, radius))
hexes.append(HexUI(board.hexes[6], center_x + 5 * radius // 3, center_y + radius, radius))

# Add OrderUIs
board.orders = [Order(Hex(1), 1, "Length", None), Order(Hex(0, 1), 1, "Mass", None), Order(Hex(0, 0, 1), 1, "Time", None)]
orders.append(OrderUI(board.orders[0], 20, 20))
orders.append(OrderUI(board.orders[1], 20, 20 + height // 3))
orders.append(OrderUI(board.orders[2], 20, 20 + 2 * height // 3))

hex_clicked_idx = -1
left_mouse_button_clicked = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Only handle left/right mouse button clicks
            if event.button not in (1, 3):
                continue
            pos = pygame.mouse.get_pos()
            
            for i, hex in enumerate(hexes):
                if hex.x - 3 * hex.radius // 4 <= pos[0] <= hex.x + 3 * hex.radius // 4 and \
                    hex.y - 3 * hex.radius // 4 <= pos[1] <= hex.y + 3 * hex.radius // 4:
                        if hex_clicked_idx < 0:
                            # Select a hex
                            hex_clicked_idx = i
                            left_mouse_button_clicked = event.button == 1
                            hex.fill_color = (32, 0, 0) if left_mouse_button_clicked else (0, 32, 0)
                            break
                        
                        # Multiply/divide
                        if left_mouse_button_clicked:
                            if board.multiplyHexes(hex_clicked_idx, i):
                                board.add_hex()
                        else:
                            if board.divideHexes(hex_clicked_idx, i):
                                board.add_hex()
                        hexes[hex_clicked_idx].fill_color = (0, 0, 0)
                        hex_clicked_idx = -1
                        
                        break

            for i, order in enumerate(orders):
                if order.getTextAndRect()[1].collidepoint(pos):
                    if hex_clicked_idx == -1:
                        break
                    
                    # Remove order if it's been completed successfully
                    if order.order.compare_to(hexes[hex_clicked_idx].hex):
                        board.refresh_order(i)
                        hexes[hex_clicked_idx].hex.clear()
                        
                    hexes[hex_clicked_idx].fill_color = (0, 0, 0)
                    hex_clicked_idx = -1
                    break
    
    screen.fill((0, 0, 0))
    for hex in hexes:
        hex.draw(screen)
    for order in orders:
        order.draw(screen)
    pygame.display.flip()
    
pygame.quit()
exit()
