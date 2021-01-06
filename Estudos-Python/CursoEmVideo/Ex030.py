# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
# resultado = n % 2
# if resultado == 0 print('O número {} é par'.format(n))
if (n % 2) == 0:
    print('{} é Par'.format(n))
else:
    print('{} é Ímpar.'.format(n))
