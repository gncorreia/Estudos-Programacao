tempo = int(input('Quantos anos tem o seu carro?\nResposta:'))
if tempo <=3:
    print('Seu carro está novo!')
else:
    print('Seu carro é muito velho!')
print('--FIM--')

# pode ser feito desse jeito tbm:

tempo = int(input('Quantos anos tem o seu carro?\nResposta:'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')