# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# seu programa deverá realizar a operação solicitada em cada caso.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while True:
    print('''Menu:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    operação = int(input('O que deseja fazer? '))
    if operação == 1:
            print('A soma entre {} e {} é igual a {}.'.format(n1, n2, n1 + n2))
    elif operação == 2:
            print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, n1 * n2))
    elif operação == 3:
        if n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
        else:
                print('{} é maior que {}'.format(n2, n1))
    elif operação == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif operação == 5:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida.')
print('Volte sempre.')

# pode fazer assim tbm:
# opção = 0
# while opção != 5:
# e faz o programa dnv