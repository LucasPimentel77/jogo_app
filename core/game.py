from screens import menu, jogar

class Game:
    def __init__(self):
        self.telas = {
            "menu": menu.tela_menu,
            "jogar": jogar.jogar
            # No futuro, adicione outras: "jogo": tela_jogo, "ranking": tela_ranking, etc
        }

    def run(self):
        tela_atual = "menu"

        while tela_atual:
            funcao_tela = self.telas.get(tela_atual)
            if funcao_tela:
                proxima_tela = funcao_tela()
                tela_atual = proxima_tela
            else:
                print(f"Erro: tela '{tela_atual}' não encontrada.")
                break
            