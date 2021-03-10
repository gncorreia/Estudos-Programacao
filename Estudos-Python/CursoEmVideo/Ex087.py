# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
soma_pares = 0
soma_terceira_coluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for colunas in range(0, 3):
        matriz[linha][colunas] = int(input(f'Digite o número da linha {linha} e coluna {colunas}: '))
print('-=' * 20)
for linha in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linha][colunas]:^5}]', end='')
        if matriz[linha][colunas] % 2 == 0:
            soma_pares = soma_pares + matriz[linha][colunas]
    print()
soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
maximo = max(matriz[1][0], matriz[1][1], matriz[1][2])
print(f'A soma dos pares é igual a {soma_pares}')
print(f'A soma dos valores na terceira coluna é igual a {soma_terceira_coluna}')
print(f'O maior valor na segunda linha é {maximo}')

