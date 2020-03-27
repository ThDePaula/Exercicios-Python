a = float(input('Diga o comprimento do lado A: '))
b = float(input('Diga o comprimento do lado B: '))
c = float(input('Diga o comprimento do lado C: '))
#Fórmula para saber se pode ser um triângulo
# BC = (b-c) < a < (b+c)
# AC = (a-c) < b < (a+c)
# AB = (a-b) < c < (a+b)
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
   print('Pode ser um triângulo!')
else:
   print('Não pode ser um triângulo!')
