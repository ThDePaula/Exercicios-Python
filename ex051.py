print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
n = int(input('Informe o 1º termo: '))
#Número que iniciará a PA.
r = int(input('Agora informe a Razão: '))
#A "razão" no caso é o número que será somado a cada vez.
decimo = n + (10 - 1) * r
#Fórmula para descobrir o décimo valor da PA.
for i in range(n, decimo + r, r):
    print(i, end=' → ')
print('FIM')