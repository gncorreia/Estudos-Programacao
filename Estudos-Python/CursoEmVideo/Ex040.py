# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 4.9:
    print('Infelizmente tu ta REPROVADO!')
elif media == 5.0 or media <= 6.9:
    print('Vá para a RECUPERAÇÃO!')
elif media >= 7.0:
    print('Parabéns! Você está APROVADO!')

# if 7 > media >= 5:
