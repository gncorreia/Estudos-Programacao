# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porçao inteira.
# Ex: Digite um numero: 6.127 O numero 6.127 tem a parte inteira 6.
# Jeito 1:
from math import trunc
num = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(num, trunc(num)))

# Jeito 2:
num = float(input('Digite um número'))
print('O número {} tem sua parte inteira {}'.format(num, int(num)))

# Jeito 3
num = float(input('Digite um número'))
print('O número {} tem a sua parte inteira {:.0f}'.format(num, num))

