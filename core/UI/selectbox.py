import pygame
from core.UI.button import Button
from core._colors import AZUL, BRANCO, CINZA, PRETO

class SelectBox(Button):
    def __init__(self, x, y, w, h, options, bg_color=AZUL, text_color=BRANCO):
        super().__init__(x, y, w, h, options[0], bg_color, text_color)
        self.options = options
        self.qtd_options = len(options)
        self.selected_index = 0
        self.expanded = False
        self.option_height = h
        self.original_text_color = text_color
        self.buttons_options = []

    def draw(self, screen):
        # Desenha a "caixa principal"
        super().draw(screen)

        # Desenha as opções se estiver expandido

        if self.expanded and len(self.buttons_options) < self.qtd_options:
            for i, option in enumerate(self.options):
                x = self.rect.x
                y = self.rect.y + (i + 1) * self.option_height 
                w = self.rect.w
                h = self.option_height

                text = option if i != self.selected_index else f"> {option} <"
                cor_fundo = self.bg_color if i != self.selected_index else CINZA

                op_button = Button(x, y, w, h, text, cor_fundo, self.original_text_color)

                if i == self.selected_index:
                    op_button.add_border(PRETO, thickness=3)

                self.buttons_options.append(op_button)

        # DESENHA os botões toda vez que expandido
        if self.expanded:
            for botao in self.buttons_options:
                botao.draw(screen)

    def add_buttons(self, buttons):
        if self.expanded:
            buttons.extend(self.buttons_options)
        else:
            self.buttons_options.clear()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_clicked(event.pos):
                self.expanded = not self.expanded
            elif self.expanded:
                for i in range(len(self.options)):
                    option_rect = pygame.Rect(
                        self.rect.x, self.rect.y + (i + 1) * self.option_height,
                        self.rect.w, self.option_height
                    )
                    if option_rect.collidepoint(event.pos):
                        self.selected_index = i
                        self.text = self.options[i]  # Atualiza texto principal
                        self.expanded = False
                        break
                else:
                    self.expanded = False

    def get_selected(self):
        return self.options[self.selected_index]