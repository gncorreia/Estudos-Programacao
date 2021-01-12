# faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 0
for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi de {}kg e o menor foi de {}kg'.format(maior_peso, menor_peso))


# outro jeito

lst=[]  #lista vazia

for c in range(1, 6):

    peso=float(input('Peso da {}ª pessoa: '.format(c)))

    lst+=[peso]   #adc os valores de peso na lista

print('')

print('O Maior peso foi:', max(lst))  #maximo valor da lista

print('O Menor peso foi:', min(lst))  #minimo valor da lista

