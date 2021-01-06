# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela podem
# ou não formar um triângulo.
a = float(input('Digite o ângulo A: '))
b = float(input('Digite o ângulo B: '))
c = float(input('Digite o ângulo C: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('É possível fazer um triângulo.')
else:
    print('Não é possível fazer um triângulo.')

# pode fazer desse jeito tbm: if a < b + c and b < a + c and c < a + b: