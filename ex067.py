from time import sleep
print('-='*13)
print('TABUADA DO SEU NÚMERO')
print('-='*13)
while True:
    i = 1
    mult = 0
    num = int(input('Deseja ver a tabuda de qual valor? '))
    if num <= -1:
        break
    print('-'*20)
    while i <= 10:
        mult = num * i 
        print(f'{num} x {i} = {mult}')
        i += 1
    print('-'*20)
print('Aguarde...')
sleep(2)
print('Programa Finalizado com sucesso!')
