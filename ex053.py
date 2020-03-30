print('='*25)
print('A FRASE É UM PALÍNDROMO?')
print('='*25)
frase = str(input('Digite uma frase: ')).strip().upper() #Lendo sem espaços ínuteis e com tudo em caixa alta.
palavras = frase.split() #Separando por frase.
frase_junta = ''.join(palavras) #Juntando a frase em uma só palavra.
inverso = ''
for letra in range(len(frase_junta) - 1, -1, -1):
    inverso += frase_junta[letra]
if inverso == frase_junta:
    print(frase_junta, '→', inverso)
    print('A frase é um Palíndromo!')
else:
    print(frase_junta, '→', inverso)
    print('A frase NÃO é um Palíndromo!')
