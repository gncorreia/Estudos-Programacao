# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LOJA DO GABRIEL'))
preço = float(input('Digite o preço total da compra: R$'))
metodo = int(input('''Como deseja pagar?
(1) À vista dinhero/cheque
(2) À vista no cartão
(3) 2x no cartão
(4) 3x ou mais no cartão
Resposta: '''))
if metodo == 1:
    total = preço - (preço * 10 / 100)
    print('O preço à vista no dinheiro/cheque, com 10% de desconto, é R${:.2f}'.format(total))
elif metodo == 2:
    total = preço - (preço * 5 / 100)
    print('O preço à vista no cartão, com 5% de desconto é R${:.2f}'.format(total))
elif metodo == 3:
    print('O preço em até 2x no cartão é R${:.2f}'.format(preço))
elif metodo == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preço + (preço * 20 / 100)
    total = juros / parcelas
    print('O preço final da compra parcelada em {}x de R${:.2f}, com 20% de juros, no cartão é R${:.2f}'.format(parcelas, total, juros))
else:
    print('Digite um metodo válido.')



