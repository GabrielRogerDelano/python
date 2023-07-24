precoUnitario = 10 
#eval transforma a string em numero
quantidade = eval(input('\n\n\n\n\n\nDigite a quantidade que vai comprar : \n'))

if (quantidade <= 10):
    ValorFinal = quantidade * precoUnitario 

elif(quantidade <= 20):
    ValorFinal = quantidade * precoUnitario * (1-0.1)
else:
    ValorFinal = quantidade * precoUnitario * (1-0.2)

print(f'o valor final da conta é R${ValorFinal}')