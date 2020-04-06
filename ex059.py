from time import sleep
n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
resp = '1'
while resp != '5':
    print('='*23)
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Pragrama''')
    print('='*23)
    resp = str(input('Selecione sua opção: '))
    if resp == '1':
        soma = n1 + n2
        print('Soma entre os números informados: {}'.format(soma))
    elif resp == '2':
        mult = n1 * n2
        print('Multiplicação entre os números informados: {}'.format(mult))
    elif resp == '3':
        if n1 > n2:
            print('Dos números informados o {} é o maior'.format(n1))
        else:
            print('Dos números informados o {} é o maior'.format(n2))
    elif resp == '4':
        n1 = int(input('Informe o 1º número: '))
        n2 = int(input('Informe o 2º número: '))
    elif resp == '5':
        print('Finalizando...')
    else:
        print('ops! digito errado erro!')
sleep(2)
print('Volte sempre :)')
