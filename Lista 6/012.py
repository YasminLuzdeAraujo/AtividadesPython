numeros = [5, 2, 8, 1, 9, 3]
maior = numeros[0]
menor = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(maior, menor)