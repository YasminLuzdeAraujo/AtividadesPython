import numpy as np

ingredientes = np.array([[2, 1, 3], [4, 2, 1]])
pedidos = np.array([[5, 2], [3, 4], [1, 6]])
resultado = np.dot(ingredientes, pedidos)

print('Ingredientes:')
print(ingredientes)
print('Pedidos:')
print(pedidos)
print('Resultado:')
print(resultado)