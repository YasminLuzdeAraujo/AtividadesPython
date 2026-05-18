matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escalar = float(input('Digite um número: '))
for linha in matriz:
    nova = [n * escalar for n in linha]
    print(nova)
