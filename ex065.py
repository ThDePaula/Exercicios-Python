resp = 'S'
soma = 0
media = 0
quant = 0
while resp in 'S':
    n = int(input('Informe um valor: '))
    soma += n
    quant += 1
    resp = str(input('Deseja continuar? [N/s] ')).strip().upper()[0]
med = soma / quant
print('Média dos números: {}'.format(med))