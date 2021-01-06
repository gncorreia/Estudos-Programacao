# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
# maior
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número é {}'.format(n3))
#menor
if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número é {}'.format(n3))

# dá pra simplificar assumindo que menor ou maior = a e ir testanto isso
# menor = a
# if b < a and b < c:
#   menor = b
# if c < a and c < b:
# menor = c
# dps a mesma lógica para o maior

