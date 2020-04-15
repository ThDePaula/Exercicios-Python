from random import randint
v = 0
while True:
    jogador = int(input('Diga um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'{jogador} + {computador} = {total}.')
    if escolha == 'P':
        if total %  2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você perdeu!')  
            break 
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER! Você venceu {v} vezes.')
