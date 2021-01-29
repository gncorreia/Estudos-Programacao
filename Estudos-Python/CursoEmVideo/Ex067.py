# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = int(input('Qual tabuada desja ver? '))
contador = 0
multiplicador = 0
while True:
    print('-=' * 7)
    if n <= -1:
        break
    else:
        for contador in range(1, 11):
            print('{:2} x {:2} = {:2}'.format(n, contador, multiplicador))
            contador = contador + 1
            multiplicador = contador * n
    print('-=' * 7)
    n = int(input('Qual tabuada desja ver? '))
print('Programa encerrado.')





