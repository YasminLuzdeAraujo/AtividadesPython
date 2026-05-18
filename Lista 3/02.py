precos = {"arroz": 5.50, "feijão": 8.00, "macarrão": 4.00}

produto = input("Qual produto alterar? ")
novo_preco = float(input("Novo preço: "))

if produto in precos:
    precos[produto] = novo_preco

    print(precos)