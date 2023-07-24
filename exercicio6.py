#crie um sistema que determine se um numero é primo

def EPrimo(num):
    if num < 2 :
        return False
    
    i = num//2
    while( i > 1):
        if(num%i == 0):
            return False
        i = i-1
    return True

def imprimirResultado(numero , resultado):
    mensagem = f'O numero {numero} não é primo'
    if resultado :
        mensagem = f'O numero {numero} é primo'
    return mensagem

numero = 102967
resultado = EPrimo(numero)
msg = imprimirResultado(numero , resultado)
print(msg)