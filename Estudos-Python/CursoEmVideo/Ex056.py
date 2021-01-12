# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
# a media de idade do grupo.
# qual é o nome do homem mais velho.
# quantas mulheres tem menos de 20 anos
soma_idade = 0
maior_idade_homem = 0
nome_velho = 0
menor_idade_mulher = 0
for pessoa in range(1, 5):
    print('---- {} PESSOA ----'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma_idade += idade
    if pessoa == 1 and sexo in 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if idade > maior_idade_homem and sexo in 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'F' and idade < 20:
        menor_idade_mulher += 1
print('A média da idade do grupo é {} anos.'.format(soma_idade / 4))
print('O homem mais velho se chama {} e tem {} anos'.format(nome_velho, maior_idade_homem))
print('E temos {} mulheres menores de 20 anos'.format(menor_idade_mulher))

# faça uma coisa de cada vez





