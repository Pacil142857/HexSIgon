from math import cos
from math import sin
from math import tau
import pygame

def draw_hex(x, y, radius, color=(255, 255, 255)):
    return [color, [(x + radius * cos(tau * i / 6), y + radius * sin(tau * i / 6)) for i in range(6)], 1]

class HexUI:
    def __init__(self, hex, x, y, radius, hexColor=(255, 255, 255), textColor=(255, 255, 255)):
        self.hex = hex
        self.x = x
        self.y = y
        self.radius = radius
        self.hexColor = hexColor
        self.textColor = textColor
    
    def draw(self, surface):
        # Draw the hexagon
        pygame.draw.polygon(surface, *draw_hex(self.x, self.y, self.radius, self.hexColor))
        
        # Draw the text in the hexagon
        font = pygame.font.SysFont("Courier New", 40)
        text = font.render(str(hex), True, self.textColor)
        surface.blit(text, text.get_rect(center = (self.x, self.y)))