import pygame
from core.UI.button import Button
from core._colors import VERDE


def carrega_caminho_telas(mod):
    if mod == "Adição":
        arquivos = [f'images/tela_adicao/adicao{i}.png' for i in range(11)]
    elif mod == "Subtração":
        arquivos = [f'images/tela_subtracao/subtracao{i}.png' for i in range(16)]

    elif mod == "Multiplicação":
        arquivos = [f'images/tela_multiplicacao/multiplicacao{i}.png' for i in range(16)]    

    elif mod == "Divisão":
        arquivos = [f'images/tela_divisao/divisao{i}.png' for i in range(21)]

    else:
        arquivos = []
    return arquivos

def buttons_modulos(caminho, mod):
    arquivos = carrega_caminho_telas(mod)
    buttons = {}
    if caminho == arquivos[0]:
        buttons['retornar'] = Button(980, 610, 250, 60, "Retornar")
        buttons['prosseguir'] = Button(700, 530, 200, 60, "Prosseguir", VERDE)
    else:
        buttons['prosseguir'] = Button(980, 610, 250, 60, ">>>", VERDE)

    return buttons
