import pygame
from core.UI.button import Button
from screens.componentes_tela.buttons_jogar import get_categorias
from core._colors import ROXO, VERDE, AMARELO


def get_buttons_aprender():
    categorias = list(get_categorias().keys())
    collors = [VERDE, AMARELO, ROXO] 
    modulos = []
    for nivel in get_categorias().values():
        for mod in nivel:
            modulos.append(mod[1])
    
    x, y = 100, 150
    buttons = {}
    for i, categoria in enumerate(categorias):
        buttons[f'difilcudade{i}'] = Button(x, y + 160*i, 200, 100, categoria, collors[i]) 
        
    
    x, y = 345, 130
        
    for i in range(4):
        buttons[f'modulo{i}'] = Button(x + 230*i, y, 200, 140, modulos[i])
        
    x, y = 345, 280
        
    for i in range(4, 8):
        buttons[f'modulo{i}'] = Button(x + 230*(i-4), y, 200, 140, modulos[i])
        
    x, y = 345, 440
        
    for i in range(8, 12):
        buttons[f'modulo{i}'] = Button(x + 230*(i-8), y, 200, 140, modulos[i])
        
    return buttons
    
    
    