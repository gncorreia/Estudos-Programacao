# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# sem estrutura while

print('-=' * 15)
print('{:^30}'.format('BANCO DO GABRIEL'))
print('-=' * 15)
saque = int(input('Quanto deseja sacar? R$'))
cinquenta = int(saque/50) # dividir o saque por 50
saque = saque % 50 # o saque recebe o resto da divisão, do valor a ser sacado, por cinquenta
vinte = int(saque / 20) # dividir o resto da divisão do valor a ser sacado por vinte
saque = saque % 20 # o saque recebe o resto da divisão, do valor a ser sacado, por vinte
dez = int(saque / 10) # a mesma lógica do vinte e do cinquenta
saque = saque % 10
um = int(saque / 1)
saque = saque % 1
if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de R$50.')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20.')
if dez > 0:
    print(f'Total de {dez} cédulas de R$10.')
if um > 0:
    print(f'Total de {um} cédulas de R$1.')
print('-=' * 15)
print(('Volte sempre!'))

# usando estrutura While:

print('-=' * 15)
print('{:^30}'.format('BANCO DO GABRIEL'))
print('-=' * 15)
saque = int(input('Quanto deseja sacar? R$'))
total = saque
cédula_atual = 50
total_cédulas = 0
while True:
    if total >= cédula_atual:
        total = total - cédula_atual
        total_cédulas = total_cédulas + 1
    else:
        if total_cédulas > 0:
            print(f'Total de {total_cédulas} cédulas de R${cédula_atual}')
        if cédula_atual == 50:
            cédula_atual = 20
        elif cédula_atual == 20:
            cédula_atual = 10
        elif cédula_atual == 10:
            cédula_atual = 1
        total_cédulas = 0
        if total == 0:
            break
print('-=' * 15)
print(('Volte sempre!'))










