from math import pow, sqrt
a = float(input('Informe a cateto oposto: '))
b = float(input('Informe o cateto adjacente: '))
h = pow(a, 2) + pow(b, 2)
print('hipotenusa {:.2f} \nCateto Oposto {} \nCateto Adjacente {}'.format(sqrt(h), a, b))
