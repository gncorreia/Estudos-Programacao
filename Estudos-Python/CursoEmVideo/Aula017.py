# Listas (Parte 1)

num = [2, 5, 9, 1]
num[2] = 3 # substituir
num.append(7) # adiciona no final da lista
# num.sort() # crescente
# num.sort(reverse=True) # decrescente
num.insert(2, 0) # Adicionar o 0 na posição 2
# num.pop() # Elimina o último valor
# num.pop(2) # Elimina o segundo valor
num.remove(2) # Elimina o primeiro valor 2. Da pra usar com o laço for
if 4 in num:
   num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')


valores = [] # ou list() para começar uma lista vazia
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}')

for p, v in enumerate(valores):
    print(f'Na posição {p + 1} encontrei o valor {v}.')

mais_valores = list()
for cont in range(0, 5):
    mais_valores.append(int(input('Digite um valor: '))) # Colocar um valor na lista
print(mais_valores)

a = [2, 3, 4, 7]
b = a # Se colocar a[:] o Python vai criar uma cópia, e não uma ligação
b[2] = 8 # O Python faz uma ligação entre as duas listas
print(a)
print(b)
