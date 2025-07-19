import pygame
from core._colors import AZUL, BRANCO, CINZA_CLARO, PRETO

class Button:
    def __init__(self, x, y, width, height, text, bg_color=AZUL, text_color=BRANCO):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 48)
        self.bg_color = bg_color
        self.text_color = text_color
        self.original_text_color = text_color
        self.current_color = bg_color  # cor que será desenhada

        self.border_color = None
        self.border_thickness = 0

    def update_hover(self, mouse_pos, bg_collor=CINZA_CLARO, text_color=PRETO):
        if self.rect.collidepoint(mouse_pos):
            self.current_color = bg_collor  # botão mais claro no hover
            self.text_color = text_color          # texto preto no hover
        else:
            self.current_color = self.bg_color
            self.text_color = self.original_text_color

    def add_border(self, color, thickness=2):
            self.border_color = color
            self.border_thickness = thickness

    def draw(self, screen):
        if self.border_color and self.border_thickness > 0:
            pygame.draw.rect(screen, self.border_color, self.rect, width=self.border_thickness, border_radius=10)

        inner_rect = self.rect.inflate(-self.border_thickness * 2, -self.border_thickness * 2)
        pygame.draw.rect(screen, self.current_color, inner_rect, border_radius=8)
        
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
