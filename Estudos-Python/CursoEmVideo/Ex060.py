# Faça um programa que leia numero qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# primeiro jeito:
'''from math import factorial
n1 = int(input('Digite um número: '))
f = factorial(n1)
print('O fatorial de {} é {}'.format(n1, f))'''

# segundo jeito:
n1 = int(input('Digite um número: '))
contador = n1
# o contador começa com o n1 porque a fatoração sempre começar pelo número que queremos fatorar.
fatorial = 1 # multiplicação (divisão) limpa começa com 1, soma (ou subtração) limpa começa com 0.
while contador > 0:
    print(contador, end=' ')
    print(' x ' if contador > 1 else ' = ', end=' ')
    fatorial = fatorial * contador
    contador = contador - 1
if n1 == 0:
    print('Não é possível fatorar o número 0')
else:
    print(fatorial)



