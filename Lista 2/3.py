matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
n = int(input('Digite um número: '))
encontrado = False
for linha in matriz:
    if n in linha:
        encontrado = True
if encontrado:
    print('Número encontrado')
else:
    print('Número não encontrado')