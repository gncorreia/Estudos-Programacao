# A confederação Nascional de Natação precisa de um programa que leia o ano de nascimento de
# um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Júnior
# Até 20 anos: Sênior
# Acima: Master
idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Sua categoria é Mirim.')
elif idade <= 14:
    print('Sua categoria é Infantil.')
elif idade <= 19:
    print('Sua categoria é Júnior.')
elif idade <= 25:
    print('Sua categoria é Sênior.')
else:
    print('Sua categoria é Master.')


