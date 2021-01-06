# Crie um programa que leia o nome de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome completo?')).strip()
print('Seu nome com todas a letras maiúsculas: {}.'.format(nome.upper()))
print('Seu nome com todas minúsculas: {}.'.format(nome.lower()))
nospace = nome.replace(' ','')
print('Seu nome tem um total de {} letras.'.format(len(nospace)))
dividido = nome.split()
print('Seu primeiro nome tem um total de {} letras.'.format(len(dividido[0])))

# é possível fazer desse jeito tbm:
nome = str(input('Qual o seu nome completo?')).strip()
print('Seu nome com todas a letras maiúsculas: {}.'.format(nome.upper()))
print('Seu nome com todas minúsculas: {}.'.format(nome.lower()))
print('Seu nome tem um total de {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem um total de {} letras.'.format(nome.find(' ')))


