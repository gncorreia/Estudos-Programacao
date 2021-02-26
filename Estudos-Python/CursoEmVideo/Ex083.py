# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.
n = str(input('Digite a expressão matemática: '))
lista = list()
for simbolo in n:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0: # cada parenteses achou o seu par correspondente
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')

