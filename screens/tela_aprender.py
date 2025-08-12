import pygame
from core.screen import Screen
from screens.componentes_tela.buttons_aprender import get_buttons_aprender

def aprender(args=None):
    pygame.init()
    screen = Screen()  # Tela principal
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.draw_background()

        buttons = get_buttons_aprender()
        list_buttons = list(buttons.values())

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons['retornar'].is_clicked(event.pos):
                    return "menu", None
                if buttons['modulo0'].is_clicked(event.pos):
                    return "adicao", {}
                


    

        # Desenha e atualiza hover de todos os botões (inclusive opções)
        screen.draw_button(list_buttons)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()