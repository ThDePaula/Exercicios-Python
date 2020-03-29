soma = 0
pares = 0
impares = 0
for i in range(1, 7):
    num = int(input('Digite o {}º número: '.format(i)))
    if num % 2 == 0:
        soma += num
        pares += 1
print('Números pares informados: {} \nA soma dos números pares: {}'.format(pares, soma))
