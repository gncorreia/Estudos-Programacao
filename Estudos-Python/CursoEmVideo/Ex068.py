# faça um programa que jogue par ou ímpar com o computador. O Jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
from random import randint
contador_jogador = 0
contador_pc = 0
print('Vamos jogar Par ou Ímpar?')
while True:
    pc = randint(0, 10)
    print('-=' * 20)
    jogador = int(input('Digite um número: '))
    decisão = str(input('Você quer PAR ou ÍMPAR? : ')).strip().upper()
    if decisão in 'PAR':
        if (jogador + pc) % 2 == 0:
            print(f'{jogador} + {pc} é igual a {jogador + pc}')
            print('Portanto, VOCÊ GANHOU!!')
            contador_jogador += 1
        else:
            print(f'{jogador} + {pc} é igual a {jogador + pc}')
            print('Portanto, EU GANHEI!!')
            contador_pc += 1
    elif decisão in 'IMPAR':
        if (jogador + pc) % 2 != 0:
            print(f'{jogador} + {pc} é igual a {jogador + pc}')
            print('Portanto, VOCÊ GANHOU!!')
            contador_jogador += 1
        else:
            print(f'{jogador} + {pc} é igual a {jogador + pc}')
            print('Portanto, EU GANHEI!!')
            contador_pc += 1
    print('-=' * 20)
    continuar = str(input('Deseja continuar? [S/N] : ')).strip().upper()
    if continuar in 'N':
        break
print(f'Você ganhou {contador_jogador} vez(es) e eu ganhei {contador_pc} vez(es).')
# Obs: Eu sei que era pra fazer o jogo parar quando o jogardor perdesse
# mas achei mais divertido desse jeito.
# Qualquer coisa é só substituir a ''contagem_pc'' por um break.
