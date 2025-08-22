import pygame
import sqlite3
import hashlib


from core.UI.square import Square
from core.UI.button import Button
from core.UI.inputbox import InputBox
from core.text import Text
from core._colors import AZUL_CLARO, PRETO, AZUL_ESCURO, VERDE, VERMELHO, BRANCO

def widgets_login(args):
    mod = args['mod']
    widgets = {}

    if "warning" in args:
        if args['warning'][0] == "error":
            widgets['warning'] = Square(440, 650, 400, 50, args['warning'][1], VERMELHO, BRANCO, font_size=30)
        elif args['warning'][0] == "success":
            widgets['warning'] = Square(440, 650, 400, 50, args['warning'][1], VERDE, BRANCO, font_size=30)
        args.pop('warning')

    widgets['quadro'] = Square(390, 160, 500, 400, "", AZUL_CLARO)

    if mod == 'login':
        widgets['login'] = Square(490, 130, 300, 60, "Login", radius=30)
        widgets['caixa_usuario'] = InputBox(440, 255, 400, 60, titulo="Usuário", text="username")
        widgets['caixa_senha'] = InputBox(440, 405, 400, 60, titulo="Senha", text="senha", is_password=True)
        widgets['botao_entrar'] = Button(540, 530, 200, 60, "Entrar", AZUL_ESCURO, PRETO)
        widgets['botao_registrar'] = Button(755, 500, 100, 40, "Registrar", VERDE, PRETO, font_size=24)

    elif mod == 'registrar':
        widgets['registrar'] = Square(490, 130, 300, 60, "Registrar", radius=30)
        widgets['caixa_usuario'] = InputBox(440, 240, 400, 60, titulo="Usuário", text="username")
        widgets['caixa_senha'] = InputBox(440, 340, 400, 60, titulo="Senha", text="senha", is_password=True)
        widgets['caixa_confirmar_senha'] = InputBox(440, 440, 400, 60, titulo="Confirmar Senha", text="senha", is_password=True)
        widgets['botao_registrar'] = Button(540, 530, 200, 60, "Registrar", VERDE, PRETO)  
        widgets['botao_voltar'] = Button(760, 510, 100, 40, "Retornar", font_size=24)

    return widgets

def verifica_login(usuario, senha):
    # Gera o hash da senha fornecida
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    # Conecta ao banco de dados
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # Busca o usuário pelo nome
    cursor.execute("SELECT senha FROM usuario WHERE nome = ?", (usuario,))
    resultado = cursor.fetchone()


    cursor.execute(f"PRAGMA table_info(usuario)")
    colunas = [linha[1] for linha in cursor.fetchall()]

    cursor.execute("SELECT * FROM usuario WHERE nome = ?", (usuario,))
    dados_usuario = cursor.fetchone()

    args = dict(zip(colunas, dados_usuario)) if dados_usuario else {}

    print(dados_usuario)

    conn.close()

    # Verifica se o usuário existe e se a senha está correta
    if resultado:
        senha_armazenada = resultado[0]
        if senha_armazenada == senha_hash:
            return "menu", args
        else:
            args = {'warning': ("error", "Senha incorreta")}
            return "login", args
    else:
        args = {'warning': ("error", "Usuário não encontrado")}
        return "login", args

def cadastrar_usuario(usuario, senha):
    try:
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO usuario (nome, senha) VALUES (?, ?)", (usuario, senha_hash))

        conn.commit()
        return "sucesso"
    except sqlite3.IntegrityError:
        return "usuario_existente"
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return "erro"
    finally:
        conn.close()

def registrar(args, widgets):
    if args['mod'] == 'login':
        args['mod'] = 'registrar'
        return "login", args
    elif args['mod'] == 'registrar':
        usuario = widgets['caixa_usuario'].get_text()
        senha = widgets['caixa_senha'].get_text()
        confirmar_senha = widgets['caixa_confirmar_senha'].get_text()

        if usuario == "username" or usuario == "":
            args['warning'] = ("error", "Usuário não pode ser vazio")
            print("Usuário não pode ser vazio")
            return "login", args

        if senha == confirmar_senha:
            resultado = cadastrar_usuario(usuario, senha)

            if resultado == "sucesso" and senha != "senha" and senha != "":
                args['warning'] = ("success", "Usuário cadastrado com sucesso!")
                args['mod'] = 'login'
                print("Usuário cadastrado com sucesso!")
                return "login", args

            elif resultado == "usuario_existente":
                args['warning'] = ("error", "Erro! nome de usuário existente")
                print("Nome de usuário já existe.")
                return "login", args

            elif senha == "senha" or senha == "":
                args['warning'] = ("error", "Senha não pode ser vazia")
                print("Senha não pode ser vazia")
                return "login", args

            else:
                args['warning'] = ("error", "Erro ao cadastrar usuário")
                print("Erro ao cadastrar usuário")
                return "login", args
        else:
            args['warning'] = ("error", "As senhas não coincidem")
            print("As senhas não coincidem")
            return "login", args
