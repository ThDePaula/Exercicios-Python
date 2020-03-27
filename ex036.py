valor_casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do comprador? R$'))
parc_anos = int(input('Em quantos anos de financiamento? '))
parc_mes = parc_anos * 12 #Conversão do pagamentos de anos em meses.
#Se o valor da parcela exceder 30% do salário, o emprétismo é negado.
parc_pagament = valor_casa / parc_mes #Vendo o valor que será pago mensalmente
if parc_pagament > (sal * (30/100)):
    print('Valor do pagamento mensal: R${:.2f}'.format(parc_pagament))
    print('Empréstimo NEGADO!')
else:
    print('Valor do pagamento mensal: R${:.2f}'.format(parc_pagament))
    print('Empréstimo CONCEDIDO!')
