a = float(input('Diga o comprimento do lado A: '))
b = float(input('Diga o comprimento do lado B: '))
c = float(input('Diga o comprimento do lado C: '))
#Fórmula para saber se pode ser um triângulo
# BC = (b-c) < a < (b+c)
# AC = (a-c) < b < (a+c)
# AB = (a-b) < c < (a+b)
if a < b + c and b < a + c and c < a + b:
   print('Pode ser um triângulo!', end='')
   if a == b == c:
       print(' EQUILÁTERO!')
   elif a != b != c != a:
       print(' ESCALENO!')
   else:
       print(' ISÓSCELES')

else:
   print('Não pode ser um triângulo!')
