dinheiro = float(input('Quantos reais você tem na carteira? R$ '))
dolar = dinheiro / 5.02 #Contagem do dólar na época que o exercício foi feito.
print('Você pode comprar US${:.2f} :)'.format(dolar))
