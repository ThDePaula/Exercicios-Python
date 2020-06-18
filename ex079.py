listNum = list()
while True:
    num = int(input('Informe um valor: '))
    if num not in listNum:
        listNum.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!')
    resp = str(input('Deseja continuar? [S/n]: '))
    if resp in 'Nn':
        break
print(f'Valores digitados: {listNum}')