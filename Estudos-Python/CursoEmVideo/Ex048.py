# faça um programa que calcule a soma entre todos os número impares que sao multiplos de tres e que se encontram no
# intervalo de 1 até 500.
impar = 0 #acumulador
cont = 0 #contador
for n in range(1, 501, 2):
    if n % 3 == 0:
        # print(n, end=' ')
        cont += + 1
        impar += + n
print('A soma dos {} ímpares multiplos de três, de 1 a 500, é igual a {}.'.format(cont, impar))

# ou print(sum(range(3, 501, 6)))

