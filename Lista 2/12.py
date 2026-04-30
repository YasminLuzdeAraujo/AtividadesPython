matriz = [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
n = len(matriz)
simetrica = True
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
if simetrica:
    print('Matriz simétrica')
else:
    print('Matriz não simétrica')