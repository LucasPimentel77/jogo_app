import pygame
from core.screen import Screen

from core.UI.button import Button
from core.UI.square import Square
from core.UI.inputbox import InputBox
from core._colors import VERDE, AZUL_CLARO, PRETO, AZUL_ESCURO
from screens.componentes_tela.componentes_login import widgets_login, verifica_login, registrar


def tela_login(args):
    pygame.init()
    pygame.key.set_repeat(300, 50)
    screen = Screen(fundo_path="images/fundo_login.png")
    clock = pygame.time.Clock()

    if 'mod' not in args:
        args['mod'] = 'login'
    

    widgets = widgets_login(args)
    list_widgets = list(widgets.values())

    running = True
    while running:
        screen.draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if "caixa_confirmar_senha" in widgets:
                widgets['caixa_confirmar_senha'].handle_event(event)
            widgets['caixa_usuario'].handle_event(event)
            widgets['caixa_senha'].handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if "botao_entrar" in widgets:
                    if widgets['botao_entrar'].is_clicked(event.pos):
                        return verifica_login(
                            widgets['caixa_usuario'].get_text(),
                            widgets['caixa_senha'].get_text()
                        )
                if widgets['botao_registrar'].is_clicked(event.pos):
                    return registrar(args, widgets)
                if "botao_voltar" in widgets:
                    if widgets['botao_voltar'].is_clicked(event.pos):
                        args['mod'] = 'login'
                        return "login", args

        screen.filter()
        screen.draw_button(list_widgets)

        pygame.display.flip()
        clock.tick(60)
