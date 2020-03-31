maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso: {}kg \nO menor peso: {}kg'.format(maior_peso, menor_peso))
