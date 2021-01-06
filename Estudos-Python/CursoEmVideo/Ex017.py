# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa
# quadrado da hipotenusa é igual a soma dos quadrados dos catetos

# Jeito Um
'''cateto1 = float(input('Comprimeto do cateto oposto: '))
cateto2 = float(input('Comprimento do cateto adjacente: '))
hipotenusa = ((cateto1 ** 2 + cateto2 ** 2) ** (1/2))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

# Jeito Dois
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# vc pode impotar somente o hypot:
# from math import hypot
# hi = hypot(cp, ca