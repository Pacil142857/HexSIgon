import pygame

class OrderUI:
    def __init__(self, order, x, y, rect_color=(255, 255, 255), text_color=(255, 255, 255)):
        self.order = order
        self.x = x
        self.y = y
        self.rect_color = rect_color
        self.text_color = text_color
    
    def draw(self, surface):
        # Render the text
        font = pygame.font.SysFont("Courier New", 40)
        text = font.render(str(self.order), True, self.text_color)
        rect = text.get_rect(center = (self.x, self.y))
        
        # Draw the rectangle
        pygame.draw.rect(surface, self.rect_color, rect, 1, 4)
        
        # Draw the text in the rectangle
        surface.blit(text, rect)