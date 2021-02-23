# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decescente.
# c) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    condição = str(input('Deseja continuar? [S/N] '))
    while condição not in 'sSnN':
        condição = int(input('Deseja continuar? [S/N] '))
    if condição in 'nN':
        break
print('-=' * 20)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')
if 5 in lista:
    print('O cinco foi digitado e está na lista.')
else:
    print('O cinco não foi digitado e não está na lista.')
print('-=' * 20)



