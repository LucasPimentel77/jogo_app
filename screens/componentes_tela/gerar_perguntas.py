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

def verifica_lista(lista, valor):
    if valor in lista or int(valor) < 0:
        return False
    return True

def ordena_valor(a, b):
    if a <= b:
        return b, a
    return a, b
    

def gerar_perguntas(modulo):
    a = random.randint(10, 99)
    b = random.randint(10, 99)

    c = random.randint(2,10)
    d = random.randint(2,10)
    options = []
    
    lista = listar_categorias()
    
    if modulo == 'Adição':
        resposta = a + b

        text = f'Qual o resultado de {a} + {b}?'
        options.append(str(resposta))
        
        while len(options) < 4:
            option = random.randint(resposta - 5, resposta +5)
            if verifica_lista(options, str(option)):
                options.append(str(option))

        random.shuffle(options)
        
        return text, options, str(resposta)

    elif modulo == 'Subtração':
        a, b = ordena_valor(a, b)
        resposta = a - b

        text = f'Qual o resultado de {a} - {b}?'
        options.append(str(resposta))
            
        while len(options) < 4:
            option = random.randint(resposta - 5, resposta + 5)
            if verifica_lista(options, str(option)):
                options.append(str(option))

        random.shuffle(options)
            
        return text, options, str(resposta)


    elif modulo == 'Multiplicação':
        resposta = c * d

        text = f'Qual o resultado de {c} * {d}?'
        options.append(str(resposta))
            
        while len(options) < 4:
            option = random.randint(resposta - 5, resposta + 5)
            if verifica_lista(options, str(option)):
                options.append(str(option))

        random.shuffle(options)

        return text, options, str(resposta)

    elif modulo == 'Divisão':
        resposta = d
        dividendo = c * d

        text = f'Qual o resultado de {dividendo} / {c}?'
        options.append(str(resposta))
            
        while len(options) < 4:
            option = random.randint(resposta - 3, resposta + 3)
            if verifica_lista(options, str(option)):
                options.append(str(option))

        random.shuffle(options)
        
        return text, options, str(resposta)
    
    return f"Erro ao gerar pergunta - {modulo}", ["A", "B", "C", "D"]
        
   
