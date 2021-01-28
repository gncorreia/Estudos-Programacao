# Crie um programa que leia varios numeros inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao
# continuar a digitar valores.
contador = 0
soma = 0
maior = 0
menor = 0
while True:
    n1 = int(input('Digite um número: '))
    contador = contador + 1
    soma = soma + n1
    pessoa = str(input('Deseja continuar? [S/N] ')).upper()
    if pessoa in 'S':
        if contador == 1:
            maior = menor = n1
        else:
            if n1 > maior:
                maior = n1
            if n1 < menor:
                menor = n1
    elif pessoa in 'N':
        break
    elif n1 is not int:
        print('Digite um número inteiro! ')
        n1 = int(input('Digite um número: '))
media = soma / contador
print('Você digitou {} números e a média foi {}.'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


# outro jeito de fazer:
resposta = 'S'
soma = quantidade = média = maior = menor = 0
while resposta in 'Ss':
    n1 = int(input('Digite um número: '))
    soma = soma + 1
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}.'.format(quantidade, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
