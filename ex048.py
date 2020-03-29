print('Números ímpares múltiplos de três')
soma = 0
num = 0
for i in range(1, 500+1):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        num += 1
print('A soma de todos os {} números é {}'.format(num, soma))
