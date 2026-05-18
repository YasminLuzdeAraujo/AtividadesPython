def processar_dados(*args, **kwargs):
    print('Valores:', args)
    print('Dados:', kwargs)

processar_dados(1, 2, 3, nome='Yasmin', cidade='Curitiba')