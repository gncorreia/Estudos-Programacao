# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
lista = []
dados = []
contador = pesados = leves = 0
while True:
    dados.append(str(input('Qual o seu nome? ')))
    dados.append(float(input('Qual o seu peso? ')))
    if len(lista) == 0:
        pesados = leves = dados[1]
    else:
        if dados[1] > pesados:
            pesados = dados[1]
        if dados[1] < leves:
            leves = dados[1]
    lista.append(dados[:])
    dados.clear()
    contador += 1
    condição = str(input('Deseja continuar? [S/N] '))
    while condição not in 'SsNn':
        condição = str(input('Deseja continuar? [S/N] '))
    if condição in 'Nn':
        break
print('-=' * 20)
print(f'No total, {contador} pessoas foram cadastradas.')
print(f'O maior peso foi de {pesados}kg. Peso de ', end='')
for pesos in lista:
    if pesos[1] == pesados:
        print(pesos[0])
print(f'O menor peso foi de {leves}kg. Peso de ', end='')
for pesos in lista:
    if pesos[1] == leves:
        print(pesos[0])

