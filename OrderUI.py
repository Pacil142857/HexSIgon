import pygame

class OrderUI:
    def __init__(self, order, x, y, rect_color=(140, 145, 183), text_color=(255, 255, 255)):
        self.order = order
        self.x = x
        self.y = y
        self.rect_color = rect_color
        self.text_color = text_color
        
    def getTextAndRect(self):
        # Render the text
        font = pygame.font.Font("JetbrainsMonoRegular-RpvmM.ttf", 35)
        text = font.render(str(self.order), True, self.text_color)
        rect = text.get_rect(topleft = (self.x, self.y))
        
        return (text, rect)
    
    def draw(self, surface):
        text, rect = self.getTextAndRect()
        
        # Draw the rectangle
        pygame.draw.rect(surface, self.rect_color, rect, 0, 4)
        
        # Draw the text in the rectangle
        surface.blit(text, rect)