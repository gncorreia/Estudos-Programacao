lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'
print(lanche[1])
print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('To de bichin chei')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('To de bichin chei')

for cont in range(0, len(lanche)):
    print(lanche[cont])

print(sorted(lanche)) # em ordem alfabética


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))
print(c.count((5))) # quantas vezes o número 5 aparece na tupla c
print(c.index(2)) # em que posição está o 2
print(c.index(5, 1)) # em que posição está o 5 depois da posição 1


pessoa = ('Gabriel', 23, 'M', 64)
# del(pessoa) # deletou da memoria
print(pessoa)


# () = tuplas
# [] = listas
# {} = dicionários