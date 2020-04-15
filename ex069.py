quant_maior = quant_homem = quant_mulher = 0
while True:
    print('='*20)
    print('CADASTRO DE PESSOAS')
    print('='*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        quant_maior += 1
    if sexo == 'M':
        quant_homem += 1
    if sexo == 'F' and idade < 20:
        quant_mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [N/s]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('¨'*35)
print(f'Pessoas com mais que 18 anos: {quant_maior}')
print(f'Homens cadastrados: {quant_homem}')
print(f'Mulheres com menos de 20 anos: {quant_mulher}')
print('¨'*35)
