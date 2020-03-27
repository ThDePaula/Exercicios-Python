num = int(input('Informe um número inteiro: '))
resp = int(input('''Converta o número informado para qual base?
[ 1 ] Para Binário
[ 2 ] Para Octal
[ 3 ] Para Hexadecimal\n'''))
if resp == 1:
    print('{} em Binário: {}'.format(num, bin(num)[2:]))
elif resp == 2:
    print('{} em Octal: {}'.format(num, oct(num)[2:]))
elif resp == 3:
    print('{} em Hexadecimal: {}'.format(num, hex(num)[2:]))
else:
    print('ERRO! Tente Novamente!')
