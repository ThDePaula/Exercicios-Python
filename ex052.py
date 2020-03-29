n = int(input('Digite um número: '))
div = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end='') #Código amarelo.
        div += 1
    else:
        print('\033[31m', end='') #Código vermelho.
    print(i, end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, div))
if div == 2: #Só é primo se for divisível por dois números.
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
