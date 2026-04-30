pares = []

for i in range(3):
    chave = input(f"Chave {i+1}: ")
    valor = input(f"Valor {i+1}: ")
    pares.append((chave, valor))

dicionario = dict(pares)
print(dicionario)