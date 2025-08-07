from screens.componentes_tela.buttons_jogar import get_categorias

lista = get_categorias().keys()
modulos = []

for nivel in get_categorias().values():
    for mod in nivel:
        print(mod[1])
        # modulos.append(mod[1])
        
print(f'\n\n{lista}\n{modulos}\n\n')
