import pygame
from core.screen import Screen
from core.question import question
from screens.componentes_tela.buttons_jogar import buttons_perguntas
from screens.componentes_tela.gerar_perguntas import gerar_perguntas

def perguntas(args):
    number = args['numero']
    modulo = args['modulo']

    esperando = False
    tempo_espera = 0
    
    botoes = buttons_perguntas(number,modulo)
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
        
        botoes['numero'].set_text(f'{number}/10')

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not esperando:
                if botoes['retornar'].is_clicked(event.pos):
                    return "menu", None
                if botoes['confirmar'].is_clicked(event.pos):
                    esperando = True
                    tempo_espera = pygame.time.get_ticks()


                    questao.paint_correct()
                    args['numero'] = questao.add_number()


                
                option = questao.get_option(event.pos)
                if option:
                    print(f'Opção selecionada: {option}')
                    if questao.is_correct():
                        print("Resposta correta!")
                    else:
                        print(f"Resposta incorreta!\nR: {questao.correct}")

        if esperando and pygame.time.get_ticks() - tempo_espera > 2000:
            return "jogo", args
        
        list_buttons = list(botoes.values())
        screen.draw_button(list_buttons)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()