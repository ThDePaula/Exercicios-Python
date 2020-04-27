cont = ('Zero', 'Um', 'Dois', 'Três', 'quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Catoze', 
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    resp = int(input('Escolha um número De 0 a 20: '))  
    if 0 <= resp <= 20:
        break
    else:
        print('Tente novamente!')      
print(f'Número escolhido foi {resp}, escrito por extenso {cont[resp]}.')
