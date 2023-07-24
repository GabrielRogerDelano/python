#encera a repeticao
for num in range(1, 11):
    if num == 5:
        break
    else:
        print(num)
print('Laço encerrado')

#pula aquela condicao repeticao
for num in range(1, 11):
    if num == 5:
        print('hit')
        continue # pass tambem da certo
    else:
        print(num)
print('Laço encerrado')