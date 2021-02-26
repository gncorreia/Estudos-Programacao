# Listas (Parte 2)
# Adicionando Listas dentro de Listas

teste = list()
teste.append('Gabriel')
teste.append('23')
galera = list()
galera.append(teste[:]) # é preciso utilizar
# os [:] para criar uma cópia da outra lista
# e não uma ligação entre as duas estruturas.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print('-=' * 30)

outra_galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(outra_galera[0])
print(outra_galera[0][0])
print(outra_galera[2][1])
print('-=' * 30)
for p in outra_galera:
    print(p) # mostrar todo mundo
print('-=' * 30)
for p in outra_galera:
    print(f'Olá, {p[0]}!') # mostra só os nomes
print('-=' * 30)
for p in outra_galera:
    print(f'{p[1]} anos de idade.') # mostrar só a idade
print('-=' * 30)

pessoas = list()
dado = list()
maior = menor = 0 # isso só é possível fazer com variáveis simples.
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)

for p in pessoas:
    # print(p)
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')






