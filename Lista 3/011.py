usuarios = {"Ana": 25, "João": 30, "Maria": 22}

opcao = ""
while opcao != "0":
    print("\n=== MENU ===")
    print("1-Exibir | 2-Buscar | 3-Adicionar | 4-Atualizar")
    print("5-Remover | 6-Copiar | 7-Limpar | 0-Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        for nome in usuarios:
            print(nome, "->", usuarios[nome])

    elif opcao == "2":
        nome = input("Nome: ")
        if nome in usuarios:
            print("Idade:", usuarios[nome])
        else:
            print("Usuário não encontrado!")

    elif opcao == "3":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        usuarios[nome] = idade
        print("Adicionado!")

    elif opcao == "4":
        nome = input("Nome: ")
        if nome in usuarios:
            usuarios[nome] = int(input("Nova idade: "))
            print("Atualizado!")
        else:
            print("Usuário não existe!")

    elif opcao == "5":
        nome = input("Nome para remover: ")
        if nome in usuarios:
            del usuarios[nome]
            print("Removido!")
        else:
            print("Usuário não encontrado!")

    elif opcao == "6":
        copia = {}
        for nome in usuarios:
            copia[nome] = usuarios[nome]
        nome = input("Qual usuário alterar na cópia? ")
        if nome in copia:
            copia[nome] = int(input("Nova idade: "))
        print("Original:", usuarios)
        print("Cópia:", copia)

    elif opcao == "7":
        if input("Confirma limpar tudo? (sim): ") == "sim":
            usuarios = {}
            print("Dicionário limpo!")

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opção inválida!")