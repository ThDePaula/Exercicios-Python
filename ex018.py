from math import radians, sin, cos, tan
ângulo = float(input("Diga um ângulo: "))
sen = sin(radians(ângulo))
cos = cos(radians(ângulo))
tan = tan(radians(ângulo))
print("Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}".format(sen, cos, tan))
