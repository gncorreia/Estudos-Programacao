# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de descont
p = float(input('Digite o preço do produto?\nR$'))
desc = (p * 5) / 100
print('Com 5% de desconto, ficara R${:.2f}!'.format(p - desc))
