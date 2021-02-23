# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
# em uma lista, já na posição correta de inserção (sem usar sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for v in range(0, 5):
    n = int(input(f'Digite o {v + 1}º número: '))
    if v == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final a lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break # é preciso colocar o break caso contrário
                # sempre será adicionado um número na determinada posição,
                # e o tamanho da lista sempre será aumentada, fazendo com que
                # pos < len(lista) eternamente.
            pos += 1
            # o len(lista) já começa como 1, quando ele passa pelo loop ele recebe + 1
            # e o pos recebe + 1, fazendo com que o len seja sempre maior.
print(f'Os valores digitados foram: {lista}')