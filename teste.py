m = float(input('Informe a distência em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('==Tabela de Medidas==')
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}m'.format(m))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
print('=' * 20)
