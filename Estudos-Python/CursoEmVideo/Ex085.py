# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e o ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = list()
for num in range(0, 7):
    n = int(input(f'Digite o {num + 1}º número: '))
    lista.append(n)
lista.sort()
print('-='* 20)
print(f'Os número pares são:', end=' ')
for pares in lista:
    if pares % 2 == 0:
        print(pares, end=' ')
print(' ')
print(f'E Os número ímpares são:', end=' ')  # arrumar a ordem crescente e a formatação dos dados
for impares in lista:
    if impares % 2 != 0:
        print(impares, end=' ')
print(' ')
print('-='* 20)

# =========================

numeros = [[], []]
for num in range(0, 7):
    n = int(input(f'Digite o {num + 1}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-=' * 20)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')
print('-='* 20)



