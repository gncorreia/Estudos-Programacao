# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/hr,
# mostre uma pensagem dizendo que ele foi multado.
# a multa vai custar R$7,00 por cada km acima do limite.
v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('Você está acima do limite! Sua multa é de {}'.format((v-80)*7))
else:
    print('Tenha um bom dia! Dirija com segurança')