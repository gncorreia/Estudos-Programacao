# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
# lidos pelo teclado. No final, mostre a matriz na tela, com a formatação
# correta.

# faça uma lista pra cada linha, pergunte para o usuário, e dps dê print
# nas respectivas posições da matriz

linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
for num in range(0, 3):
    n = int(input(f'Digite o valor para [{0}, {num}]: '))
    linha1[num].append(n)
for num in range(0, 3):
    n = int(input(f'Digite o valor para [{1}, {num}]: '))
    linha2[num].append(n)
for num in range(0, 3):
    n = int(input(f'Digite o valor para [{2}, {num}]: '))
    linha3[num].append(n)
print('A matriz formada ficou assim:')
print(linha1)
print(linha2)
print(linha3)

# ---------------

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3): # esse segundo loop será feito três vezes. assim que completado,
        # o primeiro loop será feito novamente e assim por diante.
        matriz[linha][coluna] = int(input(f'Digite um número para a Linha {linha} e Coluna {coluna}: '))
print('A matriz formada ficou assim:')
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print() # quebra de linha