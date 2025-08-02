import pygame
from core._colors import AZUL, BRANCO

class Square:
    def __init__(self, x, y, width, height, text, bg_color=AZUL, text_color=BRANCO):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 48)
        self.bg_color = bg_color
        self.text_color = text_color
        
        self.border_color = None
        self.border_thickness = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def update_hover(self, pos):
        pass
    
    def set_text(self, text):
        self.text = text
        