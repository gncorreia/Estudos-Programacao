# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e o ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = list()
for num in range(0, 7):
    n = int(input(f'Digite o {num + 1}º número: '))
    lista.append(n)
if lista in range(lista) % 2 == 0:
    print(lista)
print(lista)
