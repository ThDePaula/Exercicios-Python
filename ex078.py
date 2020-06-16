lista = []
maior = menor = 0
for cont in range(0, 5):
    lista.append(int(input(f'Informe um valor [Posição {cont}]: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print('='*30)
print(f'Valores digitados: {lista}')
print(f'Maior valor é {maior} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}.. ', end='')
print()
print(f'O Menor valor é {menor} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}.. ', end='')
print()
print('='*30)