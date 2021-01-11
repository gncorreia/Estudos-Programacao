for c in range(6, 0, -1):
    print(c)
# esse -1 um no final vai dizer que vc quer mostrar os numeros de trás pra frente.
print('-=' * 5)
for c in range(0, 7, 2):
    print(c)
# já o 2 vai dizer que vc quer mostrar os número pulando de 2 em dois.
# lembre-se que ele sempre ignora o último número, então tecnicamente ele vai mostrar, pulando de 2 em
# 2, os números de 0 a 6.
print('-=' * 5)
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
# o 'n+1' vai fazer com que seja mostrado na tela o número que vc digitou na variável. Como a função
# range ignora o último número, colocar o +1 vai fazer com que ele some um número a variável, ignore
# esse último novo número e mostre, na realidade, o número digitado na variável ''n''.
print('-=' * 5)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i , f+1, p):
    print(c)
print('-=' * 5)
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('-=' * 5)
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # ao invés tem escrever s = s + n vc pode colocar s += n
print('O somatório de todos os valores foi {}'.format(s))
print('-=' * 5)
print('Fim')


