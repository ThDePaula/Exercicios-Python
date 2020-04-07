from time import sleep
num = int(input('Informe o 1º termo: '))
#Número que iniciará a Progessão Aritmética.
razao = int(input('Informe a Razão: '))
#Número que irá somado a cada progressão.
i = 1
print('='*25)
print('Progressão Aritmética')
print('Termo inicial: {} \nRazão:{}'.format(num, razao))
print('='*25)
print('PA: {} → '.format(num), end='')
total = 0
mais = 10
while mais != 0:
    total += mais
    while i < total:
        num += razao
        print('{} → '.format(num), end='')
        i += 1
    print('Pausado')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Finalizando...')
sleep(2)
print('Progressão com {} termos mostrados.'.format(total))
print('Finalizado com sucesso!')