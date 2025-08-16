import pygame
from core.screen import Screen
from screens.componentes_tela.buttons_aprender import get_buttons_aprender
def argumentos_modulo(modulo):
    args = {}
    args['modulo'] = modulo
    args['delay'] = 750
    if modulo == "Adição":
        args["loop"] = ((6, 7, 8, 9, 10),)
        args["qtd_telas"] = 11

    elif modulo == "Subtração":
        args["loop"] = ((2,3), (4,5), (7,8,9,10), (11,12,13,14,15))
        args["qtd_telas"] = 16

    elif modulo == "Multiplicação":
        args["loop"] = ((7,8,9,10,11), (12,13,14,15))
        args["qtd_telas"] = 16
    
    elif modulo == "Divisão":
        args["loop"] = ((),)
        args["qtd_telas"] = 16

    return args

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
                    return "modulos", argumentos_modulo("Adição")
                if buttons['modulo1'].is_clicked(event.pos):
                    return "modulos", argumentos_modulo("Subtração")
                if buttons['modulo2'].is_clicked(event.pos):
                    return "modulos", argumentos_modulo("Multiplicação")
                if buttons['modulo3'].is_clicked(event.pos):
                    return "modulos", argumentos_modulo("Divisão")
                


    

        # Desenha e atualiza hover de todos os botões (inclusive opções)
        screen.draw_button(list_buttons)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()