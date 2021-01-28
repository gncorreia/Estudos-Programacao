# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma sequencia de fibonacci.
# Ex: 0, 1 , 1, 2, 3, 5, 8
print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
n = int(input('Quantos termos você quer ver? '))
contador = 3
penultimo = 1 # t1
ultimo = 1 # t2
termo = 1
print('0 -> 1 -> ', end='')
while contador <= (n):
    print('{} -> '.format(termo), end='')
    contador = contador + 1
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
print('Fim')




