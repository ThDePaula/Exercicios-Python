from math import factorial
from time import sleep
num = int(input('Calcule seu fatorial: '))
i = factorial(num)
print('Calculando...')
sleep(2)
print('{}! '.format(num), end='')
while num >= 1:
    print('{} '.format(num), end='')
    print('x ' if num >1 else '= ', end='')
    num -= 1
print('{}'.format(i))
