import pygame
from core.text import Text
from core._colors import AZUL, BRANCO

class Square:
    def __init__(self, x, y, width, height, text, bg_color=AZUL, text_color=BRANCO, radius=10, font_size=48):
        self.rect = pygame.Rect(x, y, width, height)
        self.bg_color = bg_color
        self.text_color = text_color
        self.radius = radius

        self.border_color = None
        self.border_thickness = 0

        # Cria o objeto Text e ajusta para caber no retângulo
        self.text_obj = Text(self.rect.centerx, self.rect.centery, text, color=text_color, font_size=font_size)
        self.text_obj.fit_to_rect(self.rect)

    def draw(self, screen):
        # Desenha o fundo do quadrado
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=self.radius)

        # Desenha a borda, se configurada
        if self.border_thickness > 0 and self.border_color:
            pygame.draw.rect(
                screen,
                self.border_color,
                self.rect,
                width=self.border_thickness,
                border_radius=self.radius
            )

        # Desenha o texto centralizado
        self.text_obj.draw(screen, center_pos=self.rect.center)

    def set_text(self, text):
        self.text_obj.set_text(text)
        self.text_obj.fit_to_rect(self.rect)

    def get_text(self):
        return self.text_obj.text

    def add_border(self, color, thickness=2):
        self.border_color = color
        self.border_thickness = thickness

    def remove_border(self):
        self.border_color = None
        self.border_thickness = 0

    def update_hover(self, pos):
        pass  # Pode ser implementado se quiser hover visual futuramente