n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome: {}.'.format(nome[0]))
print('Seu último nome: {}.'.format(nome[len(nome)-1]))