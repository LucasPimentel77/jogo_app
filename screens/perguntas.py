import pygame
from core.screen import Screen
from core.question import question

def perguntas():
    text = "Qual é a capital da França?"
    options = ["Paris", "Londres", "Berlim", "Madri"]
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

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()