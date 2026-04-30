matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
somas = []
for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    somas.append(soma)
print(somas)