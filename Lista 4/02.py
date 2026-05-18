import numpy as np

estoque_inicial = np.array([[50, 30, 20], [40, 25, 15], [60, 35, 10]])
vendidos = np.array([[10, 5, 8], [15, 10, 3], [20, 12, 4]])
estoque_final = estoque_inicial - vendidos

print('Estoque inicial:')
print(estoque_inicial)
print('Vendidos:')
print(vendidos)
print('Estoque final:')
print(estoque_final)