# Crie um programa que leia varios numeros inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao
# continuar a digitar valores.
condição = True
soma = 0
while condição != False:
    n1 = int(input('Digite um número.'))
    média = soma + n1
    pessoa = str(input('Deseja continuar? [S/N] ')).upper()
    if pessoa in 'S':

    else:
        condição = False



print(média)