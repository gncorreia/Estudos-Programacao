# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
# qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
for palavras in range(0, 5):
    lista.append(int(input('Digite um número: ')))
máximo = max(lista)
mínimo = min(lista)
posição1 = 0
posição2 = 0
for p, v in enumerate(lista):
    if v == máximo:
        posição1 = p
    if v == mínimo:
        posição2 = p
print(f'Os números digitados foram: {lista}')
print(f'O maior número digitado foi {máximo} na posição {posição1 + 1}.')
print(f'O menor número digitado foi {mínimo} na posição {posição2 + 1}.')

