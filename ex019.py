from random import choice
a1 = input('1º Aluno: ')
a2 = input('2º Aluno: ')
a3 = input('3º Aluno: ')
a4 = input('4º Aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
