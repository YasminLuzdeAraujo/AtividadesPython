numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maior_soma = numeros[0]
soma_atual = numeros[0]
for n in numeros[1:]:
    soma_atual = max(n, soma_atual + n)
    if soma_atual > maior_soma:
        maior_soma = soma_atual
print(maior_soma)