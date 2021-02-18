# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ( 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
        'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in tupla:
        print(f'\nNa palavra {p} temos as vogais ', end='')
        for letra in p: # como p está em uma tupla, esse laço vai analisar cada palavra e ver se elas possuem alguma vogal.
                if letra in 'AEIOU':
                        print(letra, end=' ')


