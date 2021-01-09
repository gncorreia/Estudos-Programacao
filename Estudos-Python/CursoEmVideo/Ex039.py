# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alista ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento.
# Seu programa também devará mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
gen = int(input('Você é (1) Homem ou (2) Mulher? '))
idade = date.today().year - ano
if gen == 2:
    print('Você não precisa de alistar.')
elif idade < 18 and genero == HOMEM:
    print('Ainda está cedo para se alistar, volta daqui {} anos'.format(18 - idade))
elif idade == 18 and genero == HOMEM:
    print('Meu jovem, aliste-se IMEDIATAMENTE!')
elif idade > 18:
    print('Vish... Agora não tem como fugir, você está {} anos atrasado.\nBoa Sorte.'.format(idade - 18))


# print((18 - idade) + date.today().year)
# modificar o programa pra identificar se é homem ou mulher


