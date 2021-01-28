# Interrompendo repetições While

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
# print('A soma vale {}'.format(s))

# Python Enhancement Proposal
# f strings
print(f'A soma vale {s}')
# Interpolação dentro de strings
print('-=' * 15)
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') # Python 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print('O %s tem %d anos.' % (nome, idade)) # Python 2



