AZUL = (0, 128, 255)
AZUL_CLARO = (173, 216, 230)
AMARELO = (255, 215, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
CINZA_CLARO = (230, 230, 230)
VERDE_CLARO = (144, 255, 144)
ROXO = (128, 0, 128)

def translucent_color(color, alpha):
    return (color[0], color[1], color[2], alpha)
# Adicionando o branco semi-transparente para o filtro
# BRANCO_SEMI_TRANSPARENTE = (255, 255, 255, 100)
# BRANCO70 = (255, 255, 255, 180)
# AZUL_ST = (0, 128, 255, 100)