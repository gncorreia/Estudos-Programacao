# faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
# número primo: divisivel por 1 e por ele mesmo
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1 # ele vai ficar somando +1 sempre quando um valor por divisível por c
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('Portanto, {} é um número primo'.format(num))
else:
    print('Portanto, {} não é um número primo'.format(num))

