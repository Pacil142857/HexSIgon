from math import cos, floor
from math import sin
from math import tau
from turtle import color
from Hex import Hex
import pygame
import numpy as np
import colorsys


def draw_hex(x, y, radius, w=1, color=(255, 255, 255)):
    return [color, [(x + radius * cos(tau * i / 6), y + radius * sin(tau * i / 6)) for i in range(6)], w]
def custom_dramatic_drop_interpolation(input_value):
    # Define your known points and their corresponding values
    point1 = (1, 100)
    point2 = (2, 65)
    point3 = (23, 27)
    point4 = (40, 18)

    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    x4, y4 = point4

    if input_value <= x2:
        # Linear interpolation between points 1 and 2
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        interpolated_value = a * input_value + b
    elif input_value <= x3:
        # Linear interpolation between points 2 and 3
        a = (y3 - y2) / (x3 - x2)
        b = y2 - a * x2
        interpolated_value = a * input_value + b
    elif input_value <= x4:
        # Linear interpolation between points 3 and 4
        a = (y4 - y3) / (x4 - x3)
        b = y3 - a * x3
        interpolated_value = a * input_value + b
    else:
        # Default value
        interpolated_value = y4

    return interpolated_value

    
class HexUI:
    def __init__(self, hex: Hex, x, y, radius, hex_color=(51, 50, 82), text_color=(255, 255, 255)):
        self.hex = hex
        self.x = x
        self.y = y
        self.radius = radius
        self.hex_color = hex_color
        self.text_color = text_color
        
        self.default_color = self.find_max_index_and_color(self.hex.getAsList())
        self.fill_color = self.default_color
        self.outline_color = self.fill_color


    def update(self):
        self.default_color = self.find_max_index_and_color(self.hex.getAsList())


    import colorsys
    def find_max_index_and_color(self, lst):
        # Define the RGB values for the indices
        colors = ['#f46d43', '#fdae61', '#fee08b', '#e6f598', '#abdda4', '#66c2a5', '#3288bd']

        # Check if all elements in the list are 0
        if all(x == 0 for x in lst):
            return 'light gray'

        # Find the index of the greatest integer
        max_index = lst.index(max(lst))

        # Convert the hex color code to RGB
        hex_color = colors[max_index]
        red = int(hex_color[1:3], 16)
        green = int(hex_color[3:5], 16)
        blue = int(hex_color[5:7], 16)

        return (red, green, blue)


    
    def draw(self, surface):
        self.default_color = self.find_max_index_and_color(self.hex.getAsList())
        self.fill_color = self.default_color
        
        # # Draw the hexagon
        # pygame.draw.polygon(surface, *draw_hex(self.x, self.y, self.radius+25, 0, self.hex_color))
        # pygame.draw.polygon(surface, *draw_hex(self.x, self.y, self.radius-5, 0, self.fill_color))


        #optional, for nicer edges AROUND the gigahex
        pygame.draw.polygon(surface, self.hex_color, [(self.x + (self.radius+15) * cos(2 * 3.14159 * i / 6), self.y + (self.radius+15) * sin(2 * 3.14159 * i / 6))
        for i in range(6)], 0)

        pygame.draw.polygon(surface, self.hex_color, [(self.x + self.radius * cos(2 * 3.14159 * i / 6), self.y + self.radius * sin(2 * 3.14159 * i / 6))
        for i in range(6)], 0)

        #bottom
        pygame.draw.polygon(surface, self.outline_color, [(self.x + (self.radius-15) * cos(2 * 3.14159 * i / 6), self.y + (self.radius-15) * sin(2 * 3.14159 * i / 6))
        for i in range(6)], 0)
        #top
        pygame.draw.polygon(surface, self.fill_color, [(self.x + (self.radius-40) * cos(2 * 3.14159 * i / 6), self.y + (self.radius-40) * sin(2 * 3.14159 * i / 6))
        for i in range(6)], 0)
        
        # Draw the text in the hexagon




        font = pygame.font.Font("JetbrainsMonoRegular-RpvmM.ttf", floor(custom_dramatic_drop_interpolation(len(str(self.hex)))))
        text = font.render(str(self.hex), True, self.text_color)
        surface.blit(text, text.get_rect(center = (self.x, self.y)))