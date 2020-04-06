sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print(('Valor inválido! tente novamente!'))
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Dado registrado com sucesso!')