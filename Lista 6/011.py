lista = [3, 1, 2, 1, 3, 4, 2]
sem_duplicatas = []
for item in lista:
    if item not in sem_duplicatas:
        sem_duplicatas.append(item)
print(sem_duplicatas)