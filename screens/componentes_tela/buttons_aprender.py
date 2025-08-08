import pygame
from core.UI.button import Button
from core.UI.square import Square
from screens.componentes_tela.buttons_jogar import get_categorias
from core._colors import ROXO, VERDE, AMARELO, BRANCO


def get_buttons_aprender():
    categorias = list(get_categorias().keys())
    collors = [VERDE, AMARELO, ROXO] 
    modulos = []
    for nivel in get_categorias().values():
        for mod in nivel:
            modulos.append(mod)
    
    x, y = 100, 100
    buttons = {}
    for i, categoria in enumerate(categorias):
        buttons[f'quadro{i}'] = Square(x-20, y + 210*i - 30, 1180, y + 60, categoria, collors[i])
        buttons[f'difilcudade{i}'] = Square(x, y + 210*i, 200, 100, categoria, collors[i]) 
        
    
    x, y = 345, 80
        
    for i in range(4):
        buttons[f'modulo{i}'] = Button(x + 230*i, y, 200, 140, modulos[i][1])
        buttons[f'modulo{i}'].set_multiline(symbol=modulos[i][0], label=modulos[i][1])
        
    x, y = 345, 290
        
    for i in range(4, 8):
        buttons[f'modulo{i}'] = Button(x + 230*(i-4), y, 200, 140, modulos[i][1])
        buttons[f'modulo{i}'].set_multiline(symbol=modulos[i][0], label=modulos[i][1])
    x, y = 345, 500
        
    for i in range(8, 12):
        buttons[f'modulo{i}'] = Button(x + 230*(i-8), y, 200, 140, modulos[i][1])
        buttons[f'modulo{i}'].set_multiline(symbol=modulos[i][0], label=modulos[i][1])

    buttons['retornar'] = Button(980, 650, 250, 60, "Retornar")
    return buttons
    
    
    