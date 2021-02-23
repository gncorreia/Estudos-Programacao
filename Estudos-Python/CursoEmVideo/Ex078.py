# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
# qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
for palavras in range(0, 5):
    lista.append(int(input(f'Digite a {palavras + 1}º número: ')))
máximo = max(lista)
mínimo = min(lista)
for p, v in enumerate(lista):
    if v == máximo:
        print(f'{p}, ', end='')
    if v == mínimo:
        print(f'{p}, ', end='')
print(f'Os números digitados foram: {lista}')
print(f'O maior número digitado foi {máximo} nas posições ', end='')
for p, v in enumerate(lista):
    if v == máximo:
        print(f'{p + 1}, ', end='')
print()
print(f'O menor número digitado foi {mínimo} nas posições ', end='')
for p, v in enumerate(lista):
    if v == mínimo:
        print(f'{p + 1}, ', end='')
print()

