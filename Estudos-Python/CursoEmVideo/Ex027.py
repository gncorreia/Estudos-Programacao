# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# segundo = Souza
nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print('Muito prazer te conhecer!')
print('Seu primeiro nome é {}'.format(div[0]))
print('Seu último nome é {}'.format(div[len(div)-1]))

# nesse ultimo print temos sempre que pensar o seguinte: a variavel está splitada
# e estamos pedindo para ver o length (tamanho dela) menos (-) 1
# o lenght mostra o comprimento da mensagem, vai contar a lista começando pelo 1,
# porém como ela ta splitada a contagem começa do zero (0)
# o que vai resultar sempre em: Ex: Gabriel do Nascimento Correia
# esse nome splitado vai do 0 ao 3, porem com o lenght vai do 1 ao 4
# pedindo o lenght - 1 teremos a contagem até o 4 porém com -1, ou seja, do 1 até o 3
# então sempre será mostrado a ultima string da mensagem, do input, do nome em questão
# div[len(div)-1] signigica que queremos ver sempre a ultima parte da string

