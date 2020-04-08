resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'S':
    n = int(input('Informe um valor: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n                
    resp = str(input('Deseja continuar? [N/s] ')).strip().upper()[0]
med = soma / quant
print('Você informou {} números e a média foi: {}'.format(quant, med))
print('O maior valor: {} e menor {}'.format(maior, menor))
