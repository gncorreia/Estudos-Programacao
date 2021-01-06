# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salário = float(input('Qual é o salário do funcionário? R$'))
if salário > 1250:
    print('Com o aumento de 10% seu novo salário é R${:.2f}'.format(salário + (salário * 10 / 100)))
else:
    print('Com o aumento de 15% seu novo salário é R${:.2f}'.format(salário + (salário * 15 / 100)))

