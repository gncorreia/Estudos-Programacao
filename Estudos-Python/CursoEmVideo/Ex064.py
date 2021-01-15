# Crie um programa que leia varios numeros inteiros  pelo teclado. O programa
# só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# (desconsiderando o flag).
condição_parada = 1
soma = 0
total = 0
while condição_parada != 999:
    condição_parada = int(input('Digite outro número: '))
    if condição_parada != 999:
        soma = soma + condição_parada
        total = total + 1
print('Foram digitados {} numeros, e a soma entre eles é igual a {}.'.format(total, soma))

