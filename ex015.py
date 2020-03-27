quantD = int(input('Informe a quantidade de dias alugado: '))
quantKm = float(input('Informe a quantidade de km rodados: '))
valor = (quantD * 60) + (quantKm * 0.15)
print('Valor a ser pago: R${:.2f}'.format(valor))
