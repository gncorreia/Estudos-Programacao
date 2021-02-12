# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
tupla = (n1, n2, n3, n4)
print(tupla)
print(f'O número 9 apareceu {tupla.count(9)} vez(es)')
print(f'O 3 está na posição {tupla.index(3)}')
print(f'Os números pares são: ', end='')
if n1 % 2 == 0:
    print(n1, end=' e ')
if n2 % 2 == 0:
    print(n2, end=' e ')
if n3 % 2 == 0:
    print(n3, end=' e ')
if n4 % 2 == 0:
    print(n4, end='')
