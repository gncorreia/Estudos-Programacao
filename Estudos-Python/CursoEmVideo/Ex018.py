# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse angulo.
# Jeito Um
import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cons = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O angulo {:.0f}º tem o seno de {:.2f}\nO consseno de {:.2f}\nE a tangente de {:.2f}'.format(angulo, seno, cons, tang))
# tem que passar o número para radianos

# para simplificar, vc pode importar somente o que é necessario para o programa
# from math import sin, cos, tan , radians
# dps é só tirar todas as referencias a 'math'