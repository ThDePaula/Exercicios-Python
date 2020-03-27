preco = float(input('Informe o preço do produto: R$'))
desc = preco - (preco * 5 / 100)
print('Preço normal: R${} \nPreço com 5% de desconto: R${:.2f}'.format(preco, desc))
