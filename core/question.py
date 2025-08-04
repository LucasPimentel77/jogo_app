import pygame
from core._colors import BRANCO, VERMELHO, AZUL, AZUL_CLARO,VERDE, PRETO
from core.UI.button import Button
from core.UI.square import Square

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
        self.correct_alternative = correct
        self.selected_index = 0
        self.screen = None
        self.number = number
        self.correct = None

    def get_selected(self):
        return self.options[self.selected_index]
    
    def is_correct(self):
        return self.get_selected() == self.correct_alternative
    
    def draw_question(self, screen):
        quadro = Square(390, 15, 500, 250, self.text, BRANCO, PRETO)
        screen.draw_button([quadro])

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
            if option.text == self.correct_alternative:
                option.bg_color = VERDE

    def paint_questions(self, options):
        if self.is_correct():
            options[self.number - 1][0] = "O"
            options[self.number - 1][1] = VERDE
        else:
            options[self.number - 1][0] = "X"
            options[self.number - 1][1] = VERMELHO

        return options

        
