# desenvolva um programa que leia seis numero inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for impar, desconsidere-o
soma = 0 #acumulador
# cont = 1 #contador
for n in range(1, 7):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        soma += num
        # cont += 1
print('A soma dos pares é igual a {}.'.format(soma))
