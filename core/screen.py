import pygame
from core._colors import BRANCO_SEMI_TRANSPARENTE

class Screen:
    def __init__(self, titulo='Matemática Básica', fundo_path='images/fundo_app.png'):
        self.largura = 1280
        self.altura = 720
        self.titulo = titulo

        pygame.init()
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(self.titulo)

        self.fundo = pygame.image.load(fundo_path)
        self.screen.blit(self.fundo, (0, 0))

    def draw_background(self):
        """Desenha o fundo da tela."""
        self.screen.blit(self.fundo, (0, 0))

    def filter(self, collor=BRANCO_SEMI_TRANSPARENTE):
        self.screen.blit(self.fundo, (0, 0))
        filtro = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
        filtro.fill(collor)
        self.screen.blit(filtro, (0, 0))

    def draw_button(self, buttons):
        #Desenha e atualiza todos os botões passados em uma lista.
        mouse_pos = pygame.mouse.get_pos()
        cursor_sobre_botao = False

        for botao in buttons:
            botao.update_hover(mouse_pos)
            botao.draw(self.screen)
            if botao.rect.collidepoint(mouse_pos):
                cursor_sobre_botao = True

        pygame.mouse.set_cursor(
            pygame.SYSTEM_CURSOR_HAND if cursor_sobre_botao else pygame.SYSTEM_CURSOR_ARROW
        )
