#criei um sistema qua calcule o fatorial de um numero
def calcularFatorial(num):
    f = 1
    for i in range(1,num+1):
        f = f * i
    return f

numero = eval(input('digite um numero :\n'))
print(f'\nO resultado do fatorial de {numero} é : {calcularFatorial(numero)}')