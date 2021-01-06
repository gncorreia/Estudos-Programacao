# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
# empréstimo será negado.
casa = float(input('Digite o preço da casa: R$'))
salário = float(input('Digite seu salário: R$'))
ano = int(input('Em quantos anos você vai pagar? '))
prestação_mensal = (casa / (ano * 12))
print('A prestação mensal será de R${:.2f}'.format(prestação_mensal))
if prestação_mensal > ((salário * 30) / 100):
    print('Infelizmente o empréstimo foi NEGADO')
else:
    print('O empréstimo foi CONCEDIDO')


