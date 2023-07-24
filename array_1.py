lista= [2,3,4,5,6,7]

print(lista)

print(f'a lista tem {len(lista)} numeros')
print(f'o menor numero é {min(lista)}')
print(f'e o maior numero é {max(lista)}')

for i in range(1,10):
    print(f'tem o numero {i}? : {i in lista}')