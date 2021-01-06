''' if
elif
else

if carro.esquerda():
    bloco 1

elif carro.direita():
    bloco 2

elif carro.ré
    bloco 3

else:
    bloco 4 '''

# Dentro de um if pode ser usado quantos elifs vc quiser e o else pode ser utilizado apenas uma ou
# nenhuma vez.
# Você pode ter um if sem else e com vários elifs, pode ter um if com varios elifs e com else, mas
# não pode ter um elif sem if. O Else é opcional

from time import sleep
nome = str(input('Qual o seu nome? '))
print('Hmmmm...')
sleep(1)
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana Edite':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
sleep(1)
print('Tenha um bom dia, {}!'.format(nome))



