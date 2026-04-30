matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i, linha in enumerate(matriz):
    media = sum(linha) / len(linha)
    print(f'Linha {i+1}: {media}')