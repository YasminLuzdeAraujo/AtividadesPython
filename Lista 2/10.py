matriz = [[1, 2, 3], [4, 5, 6]]
m = len(matriz)
n = len(matriz[0])
transposta = []
for j in range(n):
    linha = []
    for i in range(m):
        linha.append(matriz[i][j])
    transposta.append(linha)
print(transposta)