def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

mostrar_dados(nome='Yasmin', idade=18, cidade='Curitiba')