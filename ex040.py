nota = float(input('Informe a 1º nota: '))
nota2 = float(input('Informe a 2º nota: '))
med = (nota + nota2) / 2
if med < 5:
    print('A média foi {:.1f} \nAluno Reprovado!'.format(med))
elif med >= 5 and med <= 6.9:
    print('A média foi {:.1f} \nAluno Recuperação!'.format(med))
else:
    print('A média foi {:.1f} \nAluno Aprovado!'.format(med))
