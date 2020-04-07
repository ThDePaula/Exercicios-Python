print('-='*12)
print('SEQUÊNCIA DE FIBONACCI')
print('-='*12)
n = int(input('Quantos termos você quer ver? '))
i = 3
anterior = 0
posterior = 1
print('{} → {} '.format(anterior, posterior), end='→ ')
while i <= n:
    soma = anterior + posterior
    print('{} '.format(soma), end='→ ')
    anterior = posterior
    posterior = soma
    i += 1
print('Fim')
