from random import randint
computador = randint(0, 10) #A máquina irá pensar nos valores entre 0 a 10.
print('-'*40)
print('Pensei em um número de [0 a 10] \nTente adivinhar!')
print('-'*40)
acerto = False
tentativa = 0
while not acerto:
    jogador = int(input('Em que número eu pensei? '))
    if jogador == computador:
        print('Parabéns! Você conseguiu me vencer!')
        acerto = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente!')
    tentativa += 1
print('Você precisou de {} tentativas para me ganhar!'.format(tentativa))
