import pygame
from core.screen import Screen
from core.UI.square import Square
from core.UI.button import Button
from core._colors import BRANCO, PRETO, AZUL, VERDE_CLARO, translucent_color
from screens.componentes_tela.buttons_modulos import buttons_modulos, carrega_caminho_telas

modulo = "Subtração"
tempo_delay = 750
qtd_telas = 16

def tela_termino(screen: Screen, modulo):
    BRANCO180 = translucent_color(BRANCO, 200)
    screen.filter(BRANCO180)

    text_final = f'Você completou o aprendizado de {modulo} !'
    quadro_final = Square(240, 240, 800, 250, text_final, VERDE_CLARO, PRETO, )
    texto_modulo = Square(540, 180, 200, 120, f"{modulo}", AZUL)
    praticar_button = Button(410, 400, 200, 60, "Praticar")
    retornar_button = Button(670, 400, 200, 60, "Retornar")

    screen.draw_button([quadro_final, retornar_button, praticar_button, texto_modulo])

    return retornar_button, praticar_button

def tela_aprender_modulos(args):

    modulo = args['modulo']
    tempo_delay = args['delay']
    qtd_telas = args['qtd_telas']

    if 'arquivos' not in args:
        #loop = args['loop'] #= ((2,3), (4,5), (7,8,9,10), (11,12,13,14,15))

        args['arquivos'] = carrega_caminho_telas(modulo)
        args['indice'] = 0
    
    valores = [item for tupla in args['loop'] for item in tupla]


    if 'tempo_espera' in args:
        tempo_espera = args['tempo_espera']
    else:
        tempo_espera = False

    arquivos = args['arquivos']
    indice = args['indice']

    esperando = True if indice in valores else False
    
    final = False
    

    pygame.init()
    if indice < qtd_telas:
        screen = Screen(fundo_path=arquivos[indice])  # Tela principal
    else:
        screen = Screen()
    clock = pygame.time.Clock()
    running = True
    
    while running:
        if indice == qtd_telas:
            final = True
            botao_retornar_final, botao_praticar_final = tela_termino(screen, modulo)
            buttons = {}
        else:
            screen.draw_background()
            buttons = buttons_modulos(arquivos[indice], modulo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if final:
                    if botao_retornar_final.is_clicked(event.pos):
                        return "menu", None
                    if botao_praticar_final.is_clicked(event.pos):
                        return "jogo", {
                            "numero": "1",
                            "modulo": modulo,
                        }
                else:
                    if 'retornar' in buttons:
                        if buttons['retornar'].is_clicked(event.pos):
                            return "menu", None
                    if buttons['prosseguir'].is_clicked(event.pos):
                        if indice in valores:
                            for loop in args['loop']:
                                if indice in loop:
                                    args['indice'] = loop[-1] + 1

                        else:
                            args['indice'] += 1

                        if indice + 1 in valores:
                            tempo_espera = pygame.time.get_ticks()
                            args['tempo_espera'] = tempo_espera

                        return "modulos", args
                

        if tempo_espera:
            if esperando and pygame.time.get_ticks() - tempo_espera > tempo_delay:

                args['indice'] += 1

                for loop in args['loop']:
                    if args['indice'] == loop[-1] + 1:
                        args['indice'] = loop[0]

                tempo_espera = pygame.time.get_ticks()
                args['tempo_espera'] = tempo_espera
                return "modulos", args     
        
        screen.draw_button(list(buttons.values()))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
