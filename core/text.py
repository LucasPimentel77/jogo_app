import pygame
from core._colors import BRANCO

class Text:
    def __init__(self, x, y, text="", font_size=48, color=BRANCO):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.base_font_size = font_size
        self.font = pygame.font.Font(None, font_size)

        self.symbol = None
        self.label = None
        self.symbol_font_size = 68
        self.label_font_size = 48

    def set_text(self, text):
        self.text = text

    def set_multiline(self, symbol, label):
        self.symbol = symbol
        self.label = label

    def fit_to_rect(self, rect: pygame.Rect, font_name=None, min_font_size=10):
        """Reduz a fonte para caber no retângulo sem quebrar em linhas."""
        font_size = self.base_font_size if not self.label else self.label_font_size
        while font_size >= min_font_size:
            if not self.symbol or not self.label:
                font = pygame.font.Font(font_name, font_size)

                text_width, text_height = font.size(self.text)
                if text_width <= rect.width and text_height <= rect.height:
                    self.label_font_size = font_size
                    return
                font_size -=1
                
            else:
                text_width, text_height = font.size(f'{self.label}')
                if text_width <= rect.width and text_height <= rect.height:
                    self.font = font
                    return
                font_size -=1

        # Fonte mínima se nenhuma couber
        self.font = pygame.font.Font(font_name, min_font_size)

    def draw_multiline(self, screen, center_pos=None):
        try:
            symbol_font = pygame.font.SysFont("Segoe UI Emoji", self.symbol_font_size)
        except:
            symbol_font = pygame.font.SysFont(None, self.symbol_font_size)

        label_font = pygame.font.SysFont(None, self.label_font_size)

        symbol_surface = symbol_font.render(self.symbol, True, self.color)
        label_surface = label_font.render(self.label, True, self.color)

        if center_pos:
            symbol_rect = symbol_surface.get_rect(center=(center_pos[0], center_pos[1] - 30))
            label_rect = label_surface.get_rect(center=(center_pos[0], center_pos[1] + 30))
        else:
            symbol_rect = symbol_surface.get_rect(center=(self.x, self.y - 30))
            label_rect = label_surface.get_rect(center=(self.x, self.y + 30))

        screen.blit(symbol_surface, symbol_rect)
        screen.blit(label_surface, label_rect)

    def draw(self, screen, center_pos=None):
        if self.symbol and self.label:
            self.draw_multiline(screen, center_pos)
            return

        text_surface = self.font.render(self.text, True, self.color)

        if center_pos:
            text_rect = text_surface.get_rect(center=center_pos)
        else:
            text_rect = text_surface.get_rect(center=(self.x, self.y))

        screen.blit(text_surface, text_rect)
