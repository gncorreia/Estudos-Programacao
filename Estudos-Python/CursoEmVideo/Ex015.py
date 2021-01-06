# Escreva um program que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e 0,15 por Km rodado.
km = float(input('Quantos Km você percorreu?\nResposta: '))
dias = int(input('Por quantos dias você alugou o carro?\nResposta: '))
preço_à_pagar = (dias * 60) + (km * 0.15)
print('O custo do alugou ficou em R${:.2f}'.format(preço_à_pagar))

# vc pode dividir por parte as varias a pagar. Ex: preço_por_km e preço_por_dias e fazer as multiplicações
# em cada uma e dps somar no print; porém, da pra fazer usando menos comandos tbm.

