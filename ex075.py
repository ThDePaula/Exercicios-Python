# A seguir, a tupla
num = (int(input('Informe um número: ')),
       int(input('Informe um número: ')),
       int(input('Informe um número: ')),
       int(input('Informe um número: ')))
print(f'Você informou os valores: {num}')
# A) Quantas vezes apareceu o valor '9'
print(f'O número 9 aparece {num.count(9)} vezes')
# B) Em que posição foi digitado o primeiro valor '3'
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('Valor 3 não foi digitado')
# C) Quais números são pares
print('Números pares: ', end='')
for i in range(0, 4):
    if num[i] % 2 == 0:
        print(num[i], end=' ')
