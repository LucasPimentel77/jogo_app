import pygame
from core.screen import Screen
from screens.componentes_tela.buttons_jogar import buttons_jogar
from core._colors import BRANCO70, VERMELHO

def get_all_buttons(buttons):
    list_buttons = list(buttons.values())
    buttons["select_dificuldade"].add_buttons(list_buttons)
    return list_buttons

def set_text(categorias, buttons):
    for i, categoria in enumerate(categorias):
        symbol, label = categoria  # Desempacota a tupla
        buttons[f"categoria{i+1}"].set_text(label)
        buttons[f"categoria{i+1}"].set_multiline(symbol=symbol, label=label)
        
def get_categorias(buttons, pos):
    for i in range(1, 5):
        if buttons[f"categoria{i}"].is_clicked(pos):
            buttons[f"categoria{i}"].add_border(VERMELHO)
            for j in range(1, 5):
                if j != i:
                    buttons[f"categoria{i}"].add_border(VERMELHO, 3)
            return buttons[f"categoria{i}"].text
            
    
            


def jogar():
    pygame.init()
    screen = Screen()  # Tela principal
    clock = pygame.time.Clock()
    running = True

    # Criar um "quadro" branco translúcido
    quadro_surface = pygame.Surface((990, 680), pygame.SRCALPHA)
    quadro_surface.fill(BRANCO70)

    buttons, categorias = buttons_jogar()
    
    base = None

    while running:
        screen.draw_background()
        

        # Desenhar quadro por cima do fundo
        screen.screen.blit(quadro_surface, (270, 20))

        # Atualizar a lista completa de botões (inclusive opções expandidas)
        list_buttons = get_all_buttons(buttons)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["retornar"].is_clicked(event.pos):
                    return "menu"
                if buttons["jogar"].is_clicked(event.pos):
                    return "jogo"
                base = get_categorias(buttons,event.pos)
                buttons["select_dificuldade"].handle_event(event)

        print(base)
        # 🧠 Obter dificuldade atual e atualizar os botões de categoria
        dificuldade = buttons["select_dificuldade"].get_selected().lower()
        categorias_dificuldade = categorias.get(dificuldade, [])
        set_text(categorias_dificuldade, buttons)

        # Desenha e atualiza hover de todos os botões (inclusive opções)
        screen.draw_button(list_buttons)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
