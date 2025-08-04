from core.UI.button import Button
from core.UI.selectbox import SelectBox
from core.UI.square import Square
from core._colors import VERDE, VERMELHO, AZUL_CLARO

def get_categorias():
    return {
        "fácil": [("➕", "Adição"), ("➖", "Subtração"), ("✖️", "Multiplicação"), ("➗", "Divisão")],
        "médio": [("🔢", "Fração"), ("📏", "MMC"), ("🔀", "Regra de 3"), ("📊", "Porcentagem")],
        "difícil": [("🎲", "Probabilidade"), ("📈", "Potencia"), ("📐", "Geometria plana"), ("📦", "Geometria espacial")]
    }
     

def buttons_jogar():
    jogar = {}
    jogar["retornar"] = Button(980, 610, 250, 60, "Retornar")
    jogar["jogar"] = Button(615, 610, 250, 50, "Jogar")
    options = ["Fácil", "Médio", "Difícil"]
    jogar['select_dificuldade'] = SelectBox(25, 25, 250, 160, options, spacing=10)

    x, y, largura, altura, espaco = 355, 35, 400, 250, 50

    jogar['categoria1'] = Button(x, y, largura, altura, "Categoria 1")
    jogar['categoria2'] = Button(x, y + altura + espaco, largura, altura, "Categoria 2")
    jogar['categoria3'] = Button(x + largura + espaco, y, largura, altura, "Categoria 3")
    jogar['categoria4'] = Button(x + largura + espaco, y + altura + espaco, largura, altura, "Categoria 4")

    categorias = get_categorias()

    return jogar, categorias

def buttons_perguntas(number, modulo_escolhido, cores):
    
    dicionario = get_categorias()

    nivel_escolhido = ""    
   

    for nivel, conteudo in dicionario.items():
        for modulo in conteudo:
            if modulo[1] == modulo_escolhido:
                nivel_escolhido = nivel
    
             
                
    botoes = {}
    botoes['nivel'] = Button(15, 15, 250, 60, nivel_escolhido, VERDE)
    botoes["retornar"] = Button(15, 610, 250, 60, "Retornar")
    #botoes["confirmar"] = Button(980, 610, 250, 60, "Confirmar", VERMELHO)
    botoes["numero"] = Square(15,200, 250, 60, f"{number}/10")
    botoes["quadro"] = Square(900, 10, 365, 700, "",AZUL_CLARO)

    for i in range(1, 6):
        botoes[f"questao{i}"] = Square(925 + (i-1)*70, 250, 50, 50, cores[i-1][0], cores[i-1][1], radius=12 )
    
    for i in range(6, 11):
        botoes[f"questao{i}"] = Square(925 + (i-6)*70, 320, 50, 50, cores[i-1][0], cores[i-1][1], radius=12)

    return botoes