from math import cos
from math import sin
from math import tau
import pygame

def draw_hex(x, y, radius, w=1, color=(255, 255, 255)):
    return [color, [(x + radius * cos(tau * i / 6), y + radius * sin(tau * i / 6)) for i in range(6)], w]

class HexUI:
    def __init__(self, hex, x, y, radius, hex_color=(255, 255, 255), text_color=(255, 255, 255)):
        self.hex = hex
        self.x = x
        self.y = y
        self.radius = radius
        self.hex_color = hex_color
        self.text_color = text_color
        self.fill_color = (0, 0, 0)
    
    def draw(self, surface):
        # Draw the hexagon
        pygame.draw.polygon(surface, *draw_hex(self.x, self.y, self.radius, 0, self.hex_color))
        pygame.draw.polygon(surface, *draw_hex(self.x, self.y, self.radius-5, 0, self.fill_color))
        
        # Draw the text in the hexagon
        font = pygame.font.Font("JetbrainsMonoRegular-RpvmM.ttf", 30)
        text = font.render(str(self.hex), True, self.text_color)
        surface.blit(text, text.get_rect(center = (self.x, self.y)))