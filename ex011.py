b = float(input('Informe a largura da parede: '))
h = float(input('Informe a altura da parede: '))
A = b * h
#Sendo A = área; b = base (largura); h = altura.
#metros quadrados
quant_tinta =  (A * 1) / 2
print('Área: {}m²'.format(A))
print('Quantidade de tinta para pintar a parede: {}l'.format(quant_tinta))
