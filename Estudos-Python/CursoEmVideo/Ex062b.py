# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser que quer mostrar
# 0 termos.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
primeiro_termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(primeiro_termo), end='')
        contador = contador + 1
        primeiro_termo = primeiro_termo + razão
    print('Pausa')
    mais = int(input('Deseja saber mais quantos termos? '))
print('Programa finalizado. {} termos foram mostrados.'.format(total))









