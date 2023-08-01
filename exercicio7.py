import math
def entradaDeCados():
    coeficiente = eval(input("Digite o valor do coeficiente : "))
    return coeficiente

def calcDelta(a,b,c):
    delta = b*b - 4*a*c
    return delta

def calcRaizes(a,b,c,delta):
    if (delta < 0):
        resultado ='Nao tem raizes nos numeros reais'
    elif (delta == 0):
        x = -b / (a*2)
        resultado =f'a raiz possui apenas a raiz {x}'
    else:
        x1 = (-b + (delta ** (1/2)) / (a*2))
        x2 = (-b - (delta ** (1/2)) / (a*2))
        resultado =f'a euqcao possui as raizes {x1} e {x2}'
    return resultado


a = entradaDeCados()
b = entradaDeCados()
c = entradaDeCados()

delta = calcDelta(a,b,c)

resultado = calcRaizes(a,b,c,delta)
print(resultado)