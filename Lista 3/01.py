pessoa = {"nome": "Yasmin", "idade": 18, "cidade": "Curitiba"}

chave = input("Digite uma chave (nome, idade ou cidade):")

if chave in pessoa:
    print("Valor:", pessoa[chave])
else:
    print("Chave não encontrada!")