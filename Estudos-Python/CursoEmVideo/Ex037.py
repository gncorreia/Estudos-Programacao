# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
num = int(input('Digite um número: '))
print('''Escolha sua opção de conversão:
(1) binário
(2) octal
(3) hexadecimal''')
c = int(input('Qual será a base de conversão? '))
if c == 1:
    print('{} em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif c == 2:
    print('{} em OCTAL é {}'.format(num, oct(num)[2:]))
elif c == 3:
    print('{} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Digite uma opção válida')







