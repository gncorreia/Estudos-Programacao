# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
while True:
    n = int(input('Digite um número: '))
    while n in lista:
        n = int(input('Número já existente. Digite outro número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado à lista com sucesso!')
    condição = str(input('Deseja continuar? [S/N] '))
    while condição not in 'SsNn':
        condição = str(input('Valor inválido. Deseja continuar? [S/N] '))
    if condição in 'nN':
        break
print(f'O números, digitados, em ordem crescente são: {sorted(lista)}')

