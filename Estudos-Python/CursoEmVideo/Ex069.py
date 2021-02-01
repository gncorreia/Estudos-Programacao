# Crie um programa que leia a idade e o sexo várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
soma_18 = 0
soma_homem = 0
soma_mulheres = 0
idade = 0
while True:
    decisão = str(input('Deseja cadastrar uma pessoa? [S/N] : ')).strip().upper()
    while decisão not in 'SN':
        decisão = str(input('Deseja cadastrar uma pessoa? [S/N] : ')).strip().upper()
    if decisão in 'N':
        break
    print('-=' * 15)
    print('CADASTRO DE PESSOAS')
    print('-=' * 15)
    idade = int(input('Idade: '))
    while idade not in range(1, 100):
        idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('-=' * 15)
    if idade >= 18:
        soma_18 += 1
    if sexo in 'M':
        soma_homem += 1
    if idade < 20 and sexo in 'F':
        soma_mulheres += 1
print(f'Foram cadastrados {soma_18} pessoa(s) maior(es) de 18 anos, {soma_homem} homem(s) e {soma_mulheres} mulher(es) com menos de 18 anos.')




