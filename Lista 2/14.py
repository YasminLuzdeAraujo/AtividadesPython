a = [[1, 2], [3, 4], [5, 6]]
b = [[7, 8, 9], [10, 11, 12]]
linhas_a = len(a)
colunas_a = len(a[0])
colunas_b = len(b[0])
resultado = [[0] * colunas_b for _ in range(linhas_a)]
for i in range(linhas_a):
    for j in range(colunas_b):
        for k in range(colunas_a):
            resultado[i][j] += a[i][k] * b[k][j]
print(resultado)