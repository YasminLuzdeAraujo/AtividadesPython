matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
pares = 0
for linha in matriz:
    for n in linha:
        if n % 2 == 0:
            pares += 1
print(pares)
