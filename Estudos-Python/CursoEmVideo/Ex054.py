# crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.
from datetime import date
maior_idade = 0
menor_idade = 0
for pessoa in range(1, 8):
    ano = int(input(('Em que ano a {}ª nasceu? '.format(pessoa))))
    idade = date.today().year - ano
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('{} pessosas são maiores de idade e {} são menores'.format(maior_idade, menor_idade))



