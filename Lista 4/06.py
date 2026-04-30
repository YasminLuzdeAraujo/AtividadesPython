import numpy as np

matriz = np.array([[3, 7, 2, 5], [8, 1, 4, 6], [9, 3, 7, 2], [5, 8, 1, 4]])
matriz[:] = 1

print('Matriz com sensores ativos:')
print(matriz)