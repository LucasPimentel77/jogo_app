import pygame
from core._colors import BRANCO
from core.UI.button import Button

class question:
    def __init__(self, text, options):
        self.text = text
        self.options = options
        self.level = None
        self.module = None
        self.correct = None
        self.selected_index = 0

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
        for i, option in enumerate(self.options):
            op = Button(390, 275 + i*100, 500, 100, option)
            screen.draw_button([op])
        
    
    def draw(self, screen):
        self.draw_question(screen)
        self.draw_options(screen)

