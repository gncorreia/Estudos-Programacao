# Escreva um program que faça o computador ''pensar'' em um número inteiro de 0 a 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador.
# o programa deverá escreve na tela se o usuário venceu ou perdeu.
import random
from time import sleep
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
pc = random.randint(0,5) # faz o pc ''pensar''
player = int(input('Em que número eu pensei? '))
print('Pensando...')
sleep(2)
if player == pc:
    print('Parabéns! Você acertou!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(pc, player))