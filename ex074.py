from random import randint
num = (randint(1, 100), randint(1, 100), randint(1, 100),
        randint(1, 100), randint(1, 100)) # Listando os valores aleatórios
print('='*20)
print('Valores Gerados: ', end='')
for i in range(0, 5):
    print(num[i], end=' ')
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
