# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27
q = float(input('Quantos Reais você possue em sua carteira?\nR$'))
print('Com R${:.2f}, é possível comprar USS${:.2f} e {} Euros'.format(q, (q /3.27), (q / 4)))


# colocar a conversão de euro tbm dps
