entrada = input("Digite os nomes separados por vírgula: ")
nomes = entrada.split(",")

dicionario = dict.fromkeys(nomes, 0)
print(dicionario)