import pygame
from core.screen import Screen
from core.UI.button import Button
from core.UI.selectbox import SelectBox
from core._colors import AZUL_ST, PRETO, BRANCO70

def jogar():
    pygame.init()
    screen = Screen()  # Tela principal
    clock = pygame.time.Clock()
    running = True

    retornar = Button(980, 610, 250, 60, "Retornar")
    options = ["Fácil", "Médio", "Difícil"]
    select_dificuldade = SelectBox(25, 25, 250, 160, options, spacing=10)

    categoria1 = Button(355, 35, 400, 250, "Categoria 1")
    categoria2 = Button(355, 335, 400, 250, "Categoria 2")
    categoria3 = Button(805, 35, 400, 250, "Categoria 3")
    categoria4 = Button(805, 335, 400, 250, "Categoria 4")

    # Criar um "quadro" branco translúcido
    quadro_surface = pygame.Surface((990, 680), pygame.SRCALPHA)
    quadro_surface.fill(BRANCO70)


    buttons = [retornar, select_dificuldade, categoria1, categoria2, categoria3, categoria4]

    while running:
        screen.draw_background()

        # Desenhar quadro por cima do fundo
        screen.screen.blit(quadro_surface, (270, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retornar.is_clicked(event.pos):
                    return "menu"
                select_dificuldade.handle_event(event)

        buttons = [retornar, select_dificuldade, categoria1, categoria2, categoria3, categoria4]
        select_dificuldade.add_buttons(buttons)
        screen.draw_button(buttons)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
