import pygame
from core._colors import translucent_color, BRANCO

branco_semi_transparente = translucent_color(BRANCO, 100)

class Screen:
    def __init__(self, titulo='Matemática Básica', fundo_path='images/fundo_app.png', fundo=None):
        self.largura = 1280
        self.altura = 720
        self.titulo = titulo
        self.x = 0
        self.y = 0

        pygame.init()
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(self.titulo)

        self.fundo = pygame.image.load(fundo_path) if not fundo else fundo
        self.screen.blit(self.fundo, (0, 0))
        
    def config(self, x=0, y=0, largura=1280, altura=720):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def draw_background(self):
        """Desenha o fundo da tela."""
        self.screen.blit(self.fundo, (0, 0))

    def filter(self, collor=branco_semi_transparente):
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
