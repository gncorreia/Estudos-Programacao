# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(n, a, s))

# é possível fazer desse jeito:
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(n, (n-1), (n+41)))

# quanto menos variáveis vc usar, mais memória vc vai economizar

