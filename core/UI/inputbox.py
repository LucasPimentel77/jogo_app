import pygame
from core._colors import BRANCO, PRETO, CINZA, AZUL
from core.UI.square import Square
from core.text import Text  # sua classe Text já pronta

class InputBox:
    def __init__(self, x, y, w, h,titulo="", text="", font_size=32, is_password=False,
                 bg_color=BRANCO, text_color=PRETO, radius=10):
        
        self.rect = pygame.Rect(x, y, w, h)
        self.active = False
        self.text = text
        self.titulo = titulo
        self.text_color_next = text_color
        self.text_color = CINZA
        self.is_password = is_password

        # Square como fundo visual
        self.square = Square(x, y, w, h, "", bg_color=bg_color, text_color=self.text_color, radius=radius)
        self.square.border_thickness = 2

        # Cores de borda
        self.border_color_inactive = CINZA
        self.border_color_active = AZUL
        self.square.border_color = self.border_color_inactive

        # Text para renderizar dinamicamente
        self.titulo_object = Text(
            x + 10,           # alinhado à esquerda com um pequeno padding
            y - 30,           # acima da caixa (ajuste conforme altura da fonte)
            text=self.titulo,
            font_size=32,     # menor que o texto principal
            color=PRETO  # cinza ou qualquer cor que quiser
        )

        self.text_object = Text(x + 10, 
                                y + h // 2, 
                                "",
                                font_size=font_size, 
                                color=self.text_color
        )
        self.update_display_text()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se clicou dentro da caixa
            if self.rect.collidepoint(event.pos):

                if not self.active:
                    self.text_color = self.text_color_next
                    self.text = ""

                self.active = True
                self.square.border_color = self.border_color_active
            else:
                self.active = False
                self.square.border_color = self.border_color_inactive

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.text_object.color = self.text_color_next
            self.update_display_text()

    def update_display_text(self):
        if self.active:
            display_text = "*" * len(self.text) if self.is_password else self.text
        else:
            display_text = self.text
        self.text_object.set_text(display_text)

    def draw(self, screen):
        self.titulo_object.draw(screen)
        self.square.draw(screen)
        self.text_object.draw(screen, center_pos=(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2))

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text
        self.update_display_text()