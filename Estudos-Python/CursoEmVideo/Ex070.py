# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
total = mil = 0
menor = 0
contador = 0
mais_barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    contador += 1
    total += preço
    if preço >= 1000:
        mil += 1
    if contador == 1: # or preço < menor (pra simplificar)
        menor = preço
        mais_barato = produto
    if preço < menor:
        menor = preço
        mais_barato = produto
    condição = str(input('Deseja continuar? [S/N]')).strip().upper()
    while condição not in 'SN':
        condição = str(input('Deseja continuar? [S/N]')).strip().upper()
    if condição == 'N':
        break
print('-=' * 15)
print(f'Total da compra foi R${total:.2f}')
print(f'{mil} produtos custaram mais de R$1000.')
print(f'O produto mais barato foi o(a) {mais_barato} que custou R${menor:.2f}')
print('-=' * 15)

