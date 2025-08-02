from core.UI.button import Button
from core.UI.selectbox import SelectBox
from core.UI.square import Square
from core._colors import VERDE, VERMELHO

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

def buttons_perguntas(number, nivel):
    
    dicionario = get_categorias()
    
   

    for nivel, conteudo in dicionario.items():
        print(nivel)
        print(conteudo)
            # for modulo in nivel:
            #     print(f'\n\n{modulo}\n\n')
            #     if modulo == modulo_selecionado:
            #         nivel_selecionado = nivel
    
    
    
                
                
    botoes = {}
    botoes['nivel'] = Button(15, 15, 250, 60, nivel, VERDE)
    botoes["retornar"] = Button(15, 610, 250, 60, "Retornar")
    botoes["confirmar"] = Button(980, 610, 250, 60, "Confirmar", VERMELHO)
    botoes["numero"] = Square(15,200, 250, 60, f"{number}/10")

    return botoes