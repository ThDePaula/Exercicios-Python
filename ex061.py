num = int(input('Informe o 1º termo: '))
#Número que iniciará a Progessão Aritmética.
razao = int(input('Informe a Razão: '))
#Número que irá somado a cada progressão.
i = 1
print('='*25)
print('Progressão Aritmética')
print('Termo inicial: {} \nRazão:{}'.format(num, razao))
print('='*25)
print('PA: {} → '.format(num), end='')
while i < 10:
    num += razao
    print('{} → '.format(num), end='')
    i += 1
print('Fim')
