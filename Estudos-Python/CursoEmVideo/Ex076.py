# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços na sequencia. No final, mostre uma listagem de preços, organizando os dados
# em forma tabular.
tupla = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 10,
         'Mochila', 80,
         'Canetas', 15)
print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${tupla[pos]:>7.2f}')
print('-' * 40)
