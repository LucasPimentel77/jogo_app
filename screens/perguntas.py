import pygame
from core.screen import Screen
from core.question import question
from screens.componentes_tela.buttons_jogar import buttons_perguntas
from screens.componentes_tela.gerar_perguntas import gerar_perguntas

def perguntas(modulo):
    botoes = buttons_perguntas()
    text, options = gerar_perguntas(modulo)

    questao = question(text, options)
    
    pygame.init()
    screen = Screen()  # Tela principal
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.draw_background()
        questao.draw(screen)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botoes['retornar'].is_clicked(event.pos):
                    return "menu", None
                if botoes['confirmar'].is_clicked(event.pos):
                    return "jogo", None

        list_buttons = list(botoes.values())
        screen.draw_button(list_buttons)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()