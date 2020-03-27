print('{:=^40}'.format('Lojinha do ZÉ'))
preco = float(input('Digite o valor do produto: R$ '))
pagamento = int(input('Modo de pagamento: \n'
                      '[ 1 ] À vista no dinheiro/cheque\n'
                      '[ 2 ] À vista no cartão\n'
                      '[ 3 ] 2x no cartão\n'
                      '[ 4 ] 3x ou mais no cartão\n'
                      'Qual é a opção? '))
if pagamento == 1:
    desc = preco * (10/100)
    preco_final = preco - desc
    print('Desconto de 10% \nValor à ser pago: R${:.2f}.'.format(preco_final))
elif pagamento == 2:
    desc = preco * (5/100)
    preco_final = preco - desc
    print('Desconto de 5% \nValor à ser pago: R${:.2f}.'.format(preco_final))
elif pagamento == 3:
    preco_parce = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(preco_parce))
    print('Valor final à ser pago: R${:.2f}.'.format(preco))
elif pagamento == 4:
    quant_parcela = int(input('Quantas parcelas? '))
    juros  = preco * (20/100)
    preco_final = preco + juros
    parcela = preco_final / quant_parcela
    print('Juros de 20% \nSua compra será parcelada em {}x de R${:.2f}'.format(quant_parcela, parcela))
    print('Valor à ser pago: R${:.2f}'.format(preco_final))
else:
    print('OPAÇÃO INVÁLIDA de pagamento, tente novamente!')
print('{:=^40}'.format(''))
