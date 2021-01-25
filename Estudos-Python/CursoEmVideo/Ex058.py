# Melhore o jogo do DESAFIO 028 onde o comoutador vai "pensar" em um numero entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
random = randint(0, 10)
tentativas = 0
# jogador = int(input('Digite um número: '))
while True:
    jogador = int(input('Digite um número: '))
    tentativas += 1
    if jogador > random:
        print('Menos...')
    elif jogador < random:
        print('Mais...')
    elif jogador == random:
        print('Vc acertou!')
        break
print('Depois de {} tentivas, você acertou.'.format(tentativas))

# ou
'''
from random import randint
pc = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...')
        elif jogador > pc:
            print('Menos...')
print('Acertou com {} tentativas.'.format(palpites))
'''