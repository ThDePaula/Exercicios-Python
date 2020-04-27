times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
        'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
        'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
        'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'OS 5 PRIMEIROS COLOCADOS')
# O que foi pedido na letra A
print('-='*10)
print('OS 5 PRIMEIROS DA TABELA\n')
i = 0
for i in range(0, 5):
    print(f'{i+1}º {times[i]}')
print('-='*10)
# O que foi pedido na letra B
print(f'OS 4 ÚLTIMOS DA TABELA\n')
for i in range(16, 20):
    print(f'{i+1}º {times[i]}')
print('-='*10)
# O que foi pedido na letra C
print(f'ORDEM ALFABÉTICA\n')
for i in range(0, 20):
    print(f'{i+1}º {sorted(times)[i]}')
print('-='*10)
# O que foi pedido na letra D
print('POSIÇÃO DO TIME\n')
print(f'{times.index("Chapecoense")}º Chapecoense')
