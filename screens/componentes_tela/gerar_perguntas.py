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
    
    if modulo == 'Adição':
        text = f'qual a soma de {a} + {b}?'
        for i in range(4):
            option = random.randint(a + b - 5, a + b +5)
            options.append(option)
        options.append(a+b)
        random.shuffle(options)
        
        return text, options

    elif modulo == 'Subtração':
        text = f'qual a subtração de {a} - {b}?'
        for i in range(4):
            option = random.randint(a - b - 5, a - b + 5)
            options.append(option)
        options.append(a - b)
        random.shuffle(options)
        return text, options

    elif modulo == 'Multiplicação':
        text = f'qual o produto de {a} x {b}?'
        for i in range(4):
            option = random.randint(a * b - 20, a * b + 20)
            options.append(option)
        options.append(a * b)
        random.shuffle(options)
        return text, options

    elif modulo == 'Divisão':
        # Para evitar divisão por zero e garantir resultado inteiro
        divisor = random.randint(2, 12)
        resultado = random.randint(2, 12)
        dividendo = divisor * resultado
        text = f'qual o resultado de {dividendo} ÷ {divisor}?'
        for i in range(4):
            option = random.randint(resultado - 3, resultado + 3)
            options.append(option)
        options.append(resultado)
        random.shuffle(options)
        return text, options
    
    return f"Erro ao gerar pergunta - {modulo}", ["A", "B", "C", "D"]
        
   
