from time import sleep
num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Informe o número [999 para finalizar]: '))
    soma += num
    cont += 1
    if num == 999:
        soma -= 999
        cont -= 1
print('Okay, finalizando...')
sleep(2)
print('-='*15)
print('Números informados: {} \nSoma de todos números: {}'.format(cont, soma))
print('-='*15)