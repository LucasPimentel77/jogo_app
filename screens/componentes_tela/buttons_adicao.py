import pygame
from core.UI.button import Button
from core._colors import VERDE
# from screens.tela_adicao import carrega_caminho_telas
def carrega_caminho_telas():
    caminho = 'images/tela_adicao/'
    arquivos = ['tela_adicao.png', 'adicao1.png', 'adicao2.png', 'adicao3.png',
                'adicao4.png', 'adicao5.png', 'FORadicao6.png', 'FORadicao7.png',
                'FORadicao8.png', 'FORadicao9.png', 'FORadicao10.png']
    
    for i, arquivo in enumerate(arquivos):
        arquivos[i] = caminho + arquivo
    
    return arquivos

def buttons_adicao(caminho):
    arquivos = carrega_caminho_telas()
    buttons = {}
    if caminho == arquivos[0]:
        buttons['retornar'] = Button(980, 610, 250, 60, "Retornar")
        buttons['prosseguir'] = Button(700, 530, 200, 60, "Prosseguir", VERDE)
    else:
        buttons['prosseguir'] = Button(980, 610, 250, 60, ">>>", VERDE)

    return buttons
