quant = soma = 0
print('Finalizar a execução digite [999]')
while True:
    num = int(input('Informe um valor: '))
    if num == 999:
        break
    quant += 1
    soma += num
print('='*25)
print(f'Números informados: {quant} \nSoma dos valores: {soma}')
print('='*25)