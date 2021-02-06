# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extensão, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = int(input('Digite um número: '))
if n == 1:
    print(f'Você digitou o número {número[0]}')

else:
    while n != 1:
        print('Tente novamente.', end=' ')
        n = int(input('Digite um número válido: '))