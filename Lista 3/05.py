dados = {"a": 1, "b": 2, "c": 3}

resposta = input("Deseja apagar tudo? (sim/não): ")
if resposta == "sim":
    dados.clear()

print(dados)