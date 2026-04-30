alunos = {"Ana": 9.0, "João": 7.5, "Maria": 8.0}

nome = input("Digite o nome do aluno: ")
nota = alunos.get(nome, "Aluno não encontrado!")

print(nota)
