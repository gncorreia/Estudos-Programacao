# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra ''A''
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} na frase'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.upper().find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))

# pode colocar o .upper() antes ou depois do .strip() tbm


