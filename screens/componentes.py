from core.UI.button import Button
from core.UI.selectbox import SelectBox

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

    categorias = {
        "fácil": [("➕", "Adição"), ("➖", "Subtração"), ("✖️", "Multiplicação"), ("➗", "Divisão")],
        "médio": [("🔢", "Fração"), ("📏", "MMC"), ("🔀", "Regra de 3"), ("📊", "Porcentagem")],
        "difícil": [("🎲", "Probabilidade"), ("📈", "Potencia"), ("📐", "Geometria plana"), ("📦", "Geometria espacial")]
    }

    return jogar, categorias