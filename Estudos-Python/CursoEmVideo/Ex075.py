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
if 3 in tupla:
    print(f'O 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi encontrado.')
print(f'Os números pares são: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
