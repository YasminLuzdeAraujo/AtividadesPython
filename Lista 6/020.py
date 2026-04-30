def permutacoes(lista):
    if len(lista) <= 1:
        return [lista]
    resultado = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in permutacoes(resto):
            resultado.append([lista[i]] + p)
    return resultado

lista = [1, 2, 3]
print(permutacoes(lista))