import pygame
from core.screen import Screen
from core.UI.button import Button
from core.UI.selectbox import SelectBox
from core._colors import AZUL_ST
def jogar():
    pygame.init()
    screen = Screen()  # Inicializa a tela com fundo
    clock = pygame.time.Clock()
    running = True

    retornar = Button(980, 610, 250, 60, "Retornar")
    options = ["Fácil", "Médio", "Difícil"]
    select_dificuldade = SelectBox(25, 25, 250, 160, options, spacing=10)

    buttons = [retornar, select_dificuldade]
    

    while running:
        screen.draw_background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retornar.is_clicked(event.pos):
                    return "menu"
                select_dificuldade.handle_event(event)

        buttons = [retornar, select_dificuldade]
        select_dificuldade.add_buttons(buttons)
        
        screen.draw_button(buttons)

    
        pygame.display.flip()  # Atualiza a tela
        clock.tick(60)  # Limita a taxa de quadros

    pygame.quit()