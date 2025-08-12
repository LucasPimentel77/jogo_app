import pygame
from core.screen import Screen
from screens.componentes_tela.buttons_adicao import buttons_adicao

def carrega_caminho_telas():
    caminho = 'images/tela_adicao/'
    arquivos = ['tela_adicao.png', 'adicao1.png', 'adicao2.png', 'adicao3.png',
                'adicao4.png', 'adicao5.png', 'FORadicao6.png', 'FORadicao7.png',
                'FORadicao8.png', 'FORadicao9.png', 'FORadicao10.png']
    
    for i, arquivo in enumerate(arquivos):
        arquivos[i] = caminho + arquivo
    
    return arquivos
    

def tela_adicao(args):
    if 'arquivos' not in args:
        args['arquivos'] = carrega_caminho_telas()
        args['indice'] = 0

    if 'tempo_espera' in args:
        tempo_espera = args['tempo_espera']
    else:
        tempo_espera = False

    arquivos = args['arquivos']
    indice = args['indice']

    esperando = True if indice >= 6 else False
    
    

    pygame.init()
    screen = Screen(fundo_path=arquivos[indice])  # Tela principal
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.draw_background()
        buttons = buttons_adicao(arquivos[indice])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 'retornar' in buttons:
                    if buttons['retornar'].is_clicked(event.pos):
                        return "menu", None
                if buttons['prosseguir'].is_clicked(event.pos):
                    args['indice'] += 1

                    if indice == 5:
                        tempo_espera = pygame.time.get_ticks()
                        args['tempo_espera'] = tempo_espera

                    return "adicao", args
                

        if tempo_espera:
            if esperando and pygame.time.get_ticks() - tempo_espera > 2000:

                args['indice'] += 1
                if args['indice'] > 10:
                    args['indice'] = 6
                tempo_espera = pygame.time.get_ticks()
                args['tempo_espera'] = tempo_espera
                return "adicao", args     
        
        screen.draw_button(list(buttons.values()))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
