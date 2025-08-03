import pygame
from core._colors import BRANCO, VERMELHO, AZUL, AZUL_CLARO,VERDE
from core.UI.button import Button

class question:
    def __init__(self, text, options, correct=None, number=1):
        self.text = text
        self.options = options
        self.buttons_options = [
            Button(390, 290 + i*100 + 5*i, 500, 100, option)
            for i, option in enumerate(options)
        ]
        self.level = None
        self.module = None
        self.correct = correct
        self.selected_index = 0
        self.screen = None
        self.number = number

    def get_selected(self):
        return self.options[self.selected_index]
    
    def is_correct(self):
        return self.get_selected() == self.correct
    
    def draw_question(self, screen):
        quadro_surface = pygame.Surface((500, 250), pygame.SRCALPHA)
        quadro_surface.fill(BRANCO)
        screen.screen.blit(quadro_surface, (390, 15))

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.screen.blit(text_surface, (390, 140))

    def draw_options(self, screen):
        screen.draw_button(self.buttons_options)
        
    
    def draw(self, screen):
        self.screen = screen
        self.draw_question(screen)
        self.draw_options(screen)

    def get_option(self, pos):
        for i in range(len(self.options)):
            if self.buttons_options[i].is_clicked(pos):

                for j in range(len(self.options)):
                    self.buttons_options[j].remove_border()
                    self.buttons_options[j].bg_color = AZUL

                self.buttons_options[i].add_border(VERMELHO, 4)
                self.buttons_options[i].bg_color = AZUL_CLARO
                self.selected_index = i

                self.draw_options(self.screen)
                return self.get_selected()
            
    def add_number(self):
        if self.number < 10:
           self.number += 1
        else:
            self.number = 0
            
        return str(self.number)
        
    def paint_correct(self):
        for option in self.buttons_options:
            if option.text == self.correct:
                option.bg_color = VERDE

    def paint_questions()
        
