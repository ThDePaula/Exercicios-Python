cont = ('Zero', 'Um', 'Dois', 'Três', 'quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Catoze', 
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
resp = 'S'
while True:
    if resp in 'Ss':
        while True:
            num = int(input('Escolha um número De 0 a 20: '))  
            if 0 <= num <= 20:
                print(f'O número {num} escrito por extenso: {cont[num]}.')
                break
            else:
                print('Tente novamente!')  
    else:
        break   
    resp = str(input('Deseja constinuar [S/n] ')).upper().strip() 
