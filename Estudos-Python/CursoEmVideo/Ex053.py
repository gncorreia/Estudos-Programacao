# crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# palindromo: a frase de tras pra frente tem o mesmo significado
# Ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona.
frase = str(input('Digite uma frase: ')).upper()
if frase.replace(' ','') == frase.replace(' ','')[::-1]:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
# print(frase.replace(' ','')[::-1])
# refazer usando for
