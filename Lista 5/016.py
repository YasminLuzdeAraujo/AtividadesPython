# *args recebe qualquer quantidade de argumentos posicionais (vira uma tupla)
# **kwargs recebe argumentos nomeados (vira um dicionário)

def exemplo(*args, **kwargs):
    print(args)
    print(kwargs)

exemplo(1, 2, 3, nome='Ana', cidade='Curitiba')