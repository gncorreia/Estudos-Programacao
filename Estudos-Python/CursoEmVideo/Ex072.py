# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extensão, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
          'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número: '))
while n not in range(0, 21):
    n = int(input('Digite um número: '))

for c in range(0, 21):
    if n == c:
        print(f'Você digitou o número {número[c]}')

