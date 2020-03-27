from datetime import date
nasc = int(input('Insira o ano de nascimento do atleta: '))
ano = int(date.today().year)
idade = ano - nasc
if nasc == ano or nasc >= ano:
    print('Ano Incorreto! Tente Novamente!')
elif idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
elif idade >= 26:
    print('Categoria: MASTER')
