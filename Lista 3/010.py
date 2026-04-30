dados = {"a": 1, "b": 2, "c": 3, "d": 4}

chave = input("Qual chave remover? ")
dados.pop(chave)

dados.popitem()

nova_chave = input("Nova chave: ")
novo_valor = input("Nova valor: ")
dados.update({nova_chave: novo_valor})

print(dados)