peso = eval(input("digite seu peso"))
altura = eval(input("digite sua altura"))

imc = peso/(altura*altura)

print('seu IMC é {:4.4}'.format(imc))