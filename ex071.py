n50 = n20 = n10 = n01 = 0
print('='*20)
print('{:^20}'.format('BANCO SEJA FELIZ'))
print('='*20)
total = int(input('Informe o total desejado: R$'))
valor = total
while total >= 1:
    if total >= 50:
        total -= 50
        n50 += 1
    elif 50 >= total >= 20:
        total -= 20
        n20 += 1
    elif 20 >= total >= 10:
        total -= 10
        n10 += 1
    elif 10 >= total >= 1:
        total -= 1
        n01 +=1
print('-='*13)
print(f'Valor retirado: R${valor}')
if n50 >= 1:
    print(f'Notas de R$50: {n50}')
if n20 >= 1:
    print(f'Notas de R$20: {n20}')
if n10 >= 1:
    print(f'Notas de R$10: {n10}')
if n01 >= 1:    
    print(f'Notas de R$1: {n01}')
print('-='*13)