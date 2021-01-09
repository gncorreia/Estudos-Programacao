# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros
preço = float(input('Digite o preço total do produto: '))
método = str(input('Como deseja pagar? ')).upper
if método != À_VISTA and método != a_vista:
else:
    print('À vista no dinheiro, ou no chegue você tem 10% de desconto.')


