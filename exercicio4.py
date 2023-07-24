def encontrar_minimo(lista):
    minimo= lista[0]
    for elem in lista:  
        if (elem < minimo):
            minimo = elem
    return minimo

listaDeNumeros = [10, 2 , 5, 1 , 7] 

menor = encontrar_minimo(listaDeNumeros)
print(f'o menor numero é {menor}')