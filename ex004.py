n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(n)))
print('Só tem espaço? {}.'.format(n.isspace()))
print('É número? {}.'.format(n.isnumeric()))
print('É um alfabético? {}.'.format(n.isalpha()))
print('É alfanumérico? {}.'.format(n.isalnum()))
print('Está em maiúsculas? {}.'.format(n.isupper()))
print('Está em minúsculas? {}.'.format(n.islower()))
print('Está capitalizada? {}.'.format(n.istitle())) #Se está em caixa alta ou baixa ao mesmo tempo.
