# Desenvolva um programa que leia o primeiro termo e a razao de uma progressão aritmética.
# no final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = termo + (10 - 1) * razão
for n in range(termo, décimo + razão, razão):
    print(n, '->' ,end=' ') # pode colocar a setinha dentro do end tbm end=' -> '
print('FIM', end=' ')