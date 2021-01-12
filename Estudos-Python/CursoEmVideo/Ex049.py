# refaça o desafio 9 mostrando a tabuada de um número que o usuario escolher,
# so que agora utilizando um laço for.
tabuada = int(input('Digite a tabuada que desaja ver: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(tabuada, n, n * tabuada))
