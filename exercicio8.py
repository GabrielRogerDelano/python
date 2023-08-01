import matplotlib.pyplot as grafico

vendas = [1000 , 2000 ,1500 ,1550]
mes = ["jan" , "fev" , "marco" ,"abril"]

grafico.ylabel("vendas")
grafico.xlabel("mes")
grafico.plot(mes, vendas)
