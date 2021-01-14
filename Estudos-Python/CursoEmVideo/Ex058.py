# Melhore o jogo do DESAFIO 028 onde o comoutador vai "pensar" em um numero entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
random = randint(0, 10)
tentativas = 0
palpite = int(input('Digite um numero: '))
while palpite != random:
    print('Tente novamente')
    palpite = int(input('Digite outro número: '))
    tentativas += 1
    if palpite == random:
        print('Vc acertou!')
print('Depois de {} tentivas, você acertou.'.format(tentativas))