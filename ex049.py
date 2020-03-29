n = int(input('Qual tabuada você quer saber? '))
print('Tabuada do número {}'.format(n))
for i in range(1, 11):
    mult = n * i
    print('{} x {:2} = {}'.format(n, i, mult))
