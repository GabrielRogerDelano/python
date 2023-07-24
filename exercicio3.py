#some todos os numeros pares de uma lista
#ex : [10, 2, 5, 6, 7] = 18

def somaPares(lista):
    soma = 0
    for elem in lista:
        if(elem % 2 == 0):
            soma += elem
    return soma
    
listaDeNumeros = [10, 2, 5,6,  7]
resultado = somaPares(listaDeNumeros)
print(f'A soma de todos os pares é {resultado}')