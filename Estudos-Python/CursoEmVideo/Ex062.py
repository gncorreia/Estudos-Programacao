# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser que quer mostrar
# 0 termos.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
primeiro_termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(primeiro_termo), end='')
        contador = contador + 1
        primeiro_termo = primeiro_termo + razão
    print('PAUSA')
    mais = int(input('Deseja ver mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))








