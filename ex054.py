from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input('Ano que a {}ª pessoa nasceu: '.format(i)))
    idade = int(date.today().year) - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Quantidade de pessoas na maioridade {}'
      '\nQuantidade de pessoas não atingiram a maioridade {}'.format(maior, menor))
