import pygame
from core.UI.button import Button
from core.screen import Screen
from core._colors import AMARELO, AZUL_CLARO, PRETO

def tela_menu(args=None):
    screen = Screen()
    clock = pygame.time.Clock()
    largura = screen.largura
    altura = screen.altura

    centro_x = largura // 2
    centro_y = altura // 2

    x = 165
    y = 60

    jogar = Button(centro_x - 110, centro_y - 100, 220, 60, "Jogar", AMARELO, PRETO)
    aprender = Button(centro_x - 110, centro_y + 20, 220, 60, "Aprender", AZUL_CLARO, PRETO)
    pontuacao = Button(x, y, 250, 80, "Pontuação")
    ranking = Button(x + 350, y, 250, 80, "Ranking")
    nivel = Button(x + 700, y, 250, 80, "Nivel")

    buttons = [jogar, aprender, pontuacao, ranking, nivel]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if jogar.is_clicked(event.pos):
                    print("Botão Jogar clicado!")
                    return "jogar", None  # substitua por outra tela real quando tiver
                elif aprender.is_clicked(event.pos):
                    print("Botão Aprender clicado!")
                    return "aprender", None

        screen.filter()
        screen.draw_button(buttons)

        pygame.display.flip()
        clock.tick(60)