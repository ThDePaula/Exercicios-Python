sal = float(input('Informe o salário atual do funcionário: '))
if sal >= 1250:
   aumento = sal + ((sal * 10) / 100)
   print('O funcionário teve 10% de aumento')
   print('O salário após o aumento: R${:.2f}'.format(aumento))
else:
   aumento = sal + ((sal * 15) / 100)
   print('O funcionário teve 15% de aumento')
   print('O salário após o aumento R${:.2f}'.format(aumento))
