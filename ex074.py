from random import randint
n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)
num = (1, n2, n3, n4, n5)
print('='*20)
print('Valores Gerados: ', end='')
for i in range(0, 5):
    print(num[i], end=' ') # Listando os valores aleatórios
    if i == 0: # Caso seja a primeira rodada
        maior = num[i]
        menor = num[i]
    else:
        if num[i] > maior: # Se o número da rodada dor maior
            maior = num[i]
        if num[i] < menor: # Se o número da rodada dor menor
            menor = num[i]
print(f'\nMaior valor: {maior} \nMenor valor: {menor}')
print('='*20)
