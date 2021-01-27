# Refaça o DESAFIO 051, lendo o primeiro termo e a razao de uma PA,
# mostrando os 10 primeiros termos da progressao usando a estrutura while.
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
primeiro_termo = termo
contador = 1
while contador <= 10:
    print('{} -> '.format(primeiro_termo), end='')
    if contador == 10:
        print('Acabou', end='')
    contador = contador + 1
    primeiro_termo = primeiro_termo + razão





