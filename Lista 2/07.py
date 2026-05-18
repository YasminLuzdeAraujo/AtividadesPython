import random
matriz = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]
print(matriz)
maior = matriz[0][0]
for linha in matriz:
    for n in linha:
        if n > maior:
            maior = n
print('Maior:', maior)
