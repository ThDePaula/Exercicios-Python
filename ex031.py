distancia = float(input('Informe qual será a distância da viagem: '))
if distancia <= 200:
   valor = distancia * 0.50
   print('-'*30)
   print('Obrigado pela preferência!')
   print('Valor a ser pago: R${:.2f}'.format(valor))
   print('-'*30)
else:
   valor = distancia * 0.45
   print('-'*30)
   print('Obrigado pela preferência!')
   print('Valor a ser pago: R${:.2f}'.format(valor))
   print('-'*30)

