frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece na frase {} vezes.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez no índice {}.'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez no índice {}.'.format(frase.rfind('A')+1))
