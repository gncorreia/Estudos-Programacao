# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 != 0:
        lista_impar.append(n)
    condição = str(input('Deseja continuar? [S/N] '))
    while condição not in 'SsNn':
        condição = str(input('Deseja continuar? [S/N] '))
    if condição in 'nN':
        break
print('-=' * 20)
print(f'Foram digitados os números: {lista}')
print(f'O números pares são {lista_par}')
print(f'E os ímpares são {lista_impar}')
print('-=' * 20)