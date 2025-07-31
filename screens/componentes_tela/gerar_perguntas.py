import pygame
import random
from screens.componentes_tela.buttons_jogar import buttons_jogar

# ✅ Inicializa pygame se ainda não tiver sido iniciado
if not pygame.get_init():
    pygame.init()
if not pygame.font.get_init():
    pygame.font.init()

categorias = buttons_jogar()[1]

def listar_categorias():
    lista_categorias = []
    for nivel in categorias.values():
        for modulo in nivel:
            lista_categorias.append(modulo[1])
            
    return lista_categorias
    

def gerar_perguntas(modulo):
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    options = []
    
    lista = listar_categorias()
    
    if modulo == 'adição':
        text = f'qual a soma de {a} + {b}?'
        for i in range(4):
            option = random.randint(a + b - 5, a + b +5)
            options.append(option)
        options.append(a+b)
        random.shuffle(options)
        
        return text, options
        
   
