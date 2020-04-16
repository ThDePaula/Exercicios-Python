total = prod_caro = prod_barato = 0
nome_barato = ' '
print('='*25)
print('LOJINHA DO ZÉ')
print('='*25)
while True:
    prod_nome = str(input('Nome do Produto: '))
    prod_preco = float(input('Preço do Produto: R$')) 
    resp = ' '
    total += prod_preco
    if prod_preco >= 1000:
        prod_caro += 1
    if prod_barato == 0:
        prod_barato = prod_preco
    if prod_preco <= prod_barato:
        prod_barato = prod_preco
        nome_barato = prod_nome
    while resp not in 'NS':
        resp = str(input('Você deseja inserir mais algum produto? [N/s]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*25)
print(f'Total da Compra: R${total:.2f}')
print(f'Quantidade de produtos mais caros: {prod_caro}')
print(f'Nome do produto mais barato: {nome_barato}')
print('-'*25)
