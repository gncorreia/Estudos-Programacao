# ANSI Escape Sequence
# Ex : \033[0;33;44m]

# Style : 0, 1, 4 e 7
# 0 = None
# 1 = Bold
# 4 = Underline
# 7 = Negative

# Text = 30 ao 37
# 30 = Branco, 31 = Vermelho, 32 = Verde, 33 = Amarelo, 34 = Azul
# 35 = Roxo/Violeta, 36 = Anil, 37 = Cinza.

# Back = 40 a 47
# Mesmas cores do texto.

print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a, b))

# da pra fazer dentro do .format tbm
nome = 'Gabriel'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[34m', nome, '\033[m'))

# desse jeito tbm: criar uma lista, um dicionário
nome = 'Gabriel'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))

# mudar as cores de 10 ex e dps de todos.

