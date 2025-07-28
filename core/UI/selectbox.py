import pygame
from core.UI.button import Button
from core._colors import AZUL, BRANCO, CINZA, PRETO, VERMELHO

class SelectBox(Button):
    def __init__(self, x, y, w, h, options, bg_color=AZUL, text_color=BRANCO, mode='down', spacing=0):
        super().__init__(x, y, w, h, options[0], VERMELHO, text_color)
        self.add_border(PRETO, thickness=4)
        self.options = options
        self.qtd_options = len(options)
        self.selected_index = 0
        self.expanded = False
        self.option_height = h
        self.option_width = w
        self.original_text_color = text_color
        self.buttons_options = []

        self.bg_color = bg_color

        self.mode = mode
        self.spacing = spacing

    def update_hover(self, mouse_pos):
        super().update_hover(mouse_pos)
        if self.expanded:
            for botao in self.buttons_options:
                botao.update_hover(mouse_pos)

    def draw(self, screen):
        # Desenha a "caixa principal"
        super().draw(screen)

        # Desenha as opções se estiver expandido

        if self.expanded:
            self.buttons_options.clear()  # Limpa os antigos
            for i, option in enumerate(self.options):
                if self.mode == 'down':
                    x, y, w, h = self.down_parameters(i)
                elif self.mode == 'right':
                    x, y, w, h = self.right_parameters(i)

                cor_fundo = self.bg_color if i != self.selected_index else CINZA
                op_button = Button(x, y, w, h, option, cor_fundo, self.original_text_color)
                self.buttons_options.append(op_button)

        # DESENHA os botões toda vez que expandido
        if self.expanded:
            for botao in self.buttons_options:
                botao.draw(screen)

    def down_parameters(self, i):
        x = self.rect.x
        y = self.rect.y + (i + 1) * self.option_height  + self.spacing * (i+1)
        w = self.rect.w
        h = self.option_height

        return x, y, w, h
    
    def right_parameters(self, i):
        x = self.rect.x + (i + 1) * self.option_width + self.spacing * (i+1)
        y = self.rect.y
        w = self.rect.w
        h = self.option_height

        return x, y, w, h
    
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
                        return self.options[i]  # Retorna a opção selecionada
                        break
                else:
                    self.expanded = False
            

    def get_selected(self):
        return self.options[self.selected_index]
    
    