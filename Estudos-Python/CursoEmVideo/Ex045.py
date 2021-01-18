# Crie um programa que faça o computador jogar Jokenpô com você.
# (Pedra papel tesoura)
import random
from time import sleep
jogador = int(input('''Escolha uma das opções
(0) Pedra
(1) Papel
(2) Tesoura
Resposta: '''))
n = random.randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print(20 * '-')
if n == 0 and jogador == 2:
    print('Há! Ganhei! Joguei PEDRA e você TESOURA! Tente novamente!')
elif n == 1 and jogador == 0:
    print('Há! Ganhei! Joguei PAPEL e você jogou PEDRA! Tente novamente!')
elif n == 2 and jogador == 1:
    print('Há! Ganhei! Joguei TESOURA e você jogou PAPEL! Tente novamente!')
elif jogador == 0 and n == 2:
    print('Ok. Vocẽ jogou PEDRA, e eu TESOURA, e GANHOU! PARABÉNS!')
elif jogador == 1 and n == 0:
    print('Ok. Vocẽ jogou PAPEL, e eu PEDRA, e GANHOU! PARABÉNS!')
elif jogador == 2 and n == 1:
    print('Ok. Vocẽ jogou TESOURA, e eu PAPEL, e GANHOU! PARABÉNS!')
elif n == jogador:
    print('EMPATE! Vamos jogar novamente?')
else:
    print('Digite uma opção válida!')
print(20 * '-')


# Um jeito melhor de se fazer:
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
jogador = int(input('''Suas opções:
(0) Pedra
(1) Papel
(2) Tesoura
Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print(11 * '-=')
print('Eu joguei {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print(11 * '-=')
if computador == 0: #Pedra
   if jogador == 0:
       print('EMPATAMOS!')
   elif jogador == 1: #Papel
       print('VOCÊ GANHOU!')
   elif jogador == 2: #Tesoura
       print('EU GANHEI!')
elif computador == 1: #Papel
    if jogador == 0: #Pedra
        print('EU GANHEI!')
    elif jogador == 1:
        print('EMPATAMOS')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
elif computador == 2: #Tesoura
    if jogador == 0: #Pedra
        print('VOCÊ GANHOU')
    elif jogador == 1: #Papel
        print('EU GANHEI!')
    elif jogador == 2:
        print('EMPATAMOS')

