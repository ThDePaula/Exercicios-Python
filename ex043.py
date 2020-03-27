peso = float(input('Informe o seu peso: (Kg) '))
altura = float(input('Informe sua altura: (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso!')
elif 18.5 <= imc < 25:
    print('Parabéns, seu Peso é Ideal!')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está em Obesidade!')
elif imc >= 40:
    print('Você está em Obesidade Mórbida!!')
else:
    print('Erro')
