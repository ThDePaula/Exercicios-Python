velocidade = float(input('Velocidade do veículo (km/h): '))
if velocidade <= 80:
   print('Tudo certo por aqui!')
else:
   multa = (velocidade - 80) * 7 #A multa 1km = 7 reais
   print('Você será multado!!! \nVocê excedeu a velocidade de 80km/h \nMulta à ser paga: R${:.2f}'.format(multa))
