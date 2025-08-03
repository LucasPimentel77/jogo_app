import pygame
from core.screen import Screen
from core.question import question
from core._colors import AZUL, BRANCO, VERMELHO, translucent_color
from core.UI.button import Button
from core.UI.square import Square
from screens.componentes_tela.buttons_jogar import buttons_perguntas
from screens.componentes_tela.gerar_perguntas import gerar_perguntas

def tela_termino(screen: Screen, acertos):
    BRANCO180 = translucent_color(BRANCO, 200)
    screen.filter(BRANCO180)

    text_final = f'Você acertou {acertos} de 10 perguntas!'
    quadro_final = Square(290, 240, 700, 250, text_final, VERMELHO)
    retornar_button = Button(515, 400, 250, 60, "Retornar")

    screen.draw_button([quadro_final, retornar_button])

    return retornar_button

def perguntas(args):
    number = args['numero']
    modulo = args['modulo']
    
    if 'acertos' not in args:
        args['acertos'] = 0

    acertos = args['acertos']

    if 'colors' not in args or args['colors'] is None:
        args['colors'] = [['', AZUL] for _ in range(10)]

    color_questions = args['colors']

    modo_final = False
    botao_retornar_final = None



    esperando = False
    tempo_espera = 0
    
    botoes = buttons_perguntas(number,modulo, color_questions)
    text, options, correta = gerar_perguntas(modulo)

    questao = question(text, options, correta, number=int(number))
    print(f'Pergunta gerada: {text} com opções {options}')
    
    pygame.init()
    screen = Screen()  # Tela principal
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.draw_background()
        questao.draw(screen)
        
        if number == "0":
            modo_final = True
            botao_retornar_final = tela_termino(screen, args['acertos'])
            

        botoes['numero'].set_text(f'{number}/10')

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not esperando:

                if modo_final:
                    if botao_retornar_final and botao_retornar_final.is_clicked(event.pos):
                        return "menu", None
                else:
                    option = questao.get_option(event.pos)
                    if option:
                        botoes["confirmar"] = Button(980, 580, 250, 60, "Confirmar")
                    
                    if botoes['retornar'].is_clicked(event.pos):
                        return "menu", None
                    if 'confirmar' in botoes:
                        if botoes['confirmar'].is_clicked(event.pos):
                            esperando = True
                            tempo_espera = pygame.time.get_ticks()

                            args['colors'] = questao.paint_questions(color_questions)

                            if questao.is_correct():
                                args['acertos'] += 1

                            questao.paint_correct()
                            args['numero'] = questao.add_number()


        if esperando and pygame.time.get_ticks() - tempo_espera > 500:
            return "jogo", args
        
        list_buttons = list(botoes.values())
        screen.draw_button(list_buttons)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()