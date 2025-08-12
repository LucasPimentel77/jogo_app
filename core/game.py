from screens import menu, jogar, perguntas, tela_aprender, tela_adicao

class Game:
    def __init__(self):
        self.telas = {
            "menu": menu.tela_menu,
            "jogar": jogar.jogar,
            "jogo": perguntas.perguntas,
            "aprender": tela_aprender.aprender,
            "adicao": tela_adicao.tela_adicao
            # No futuro, adicione outras: "jogo": tela_jogo, "ranking": tela_ranking, etc
        }

    def run(self):
        tela_atual = "menu"
        args = None

        while tela_atual:
            funcao_tela = self.telas.get(tela_atual)
            if funcao_tela:
                proxima_tela, args = funcao_tela(args)
                tela_atual = proxima_tela
            else:
                print(f"Erro: tela '{tela_atual}' não encontrada.")
                break
            