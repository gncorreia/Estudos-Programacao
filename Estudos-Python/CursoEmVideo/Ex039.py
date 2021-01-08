# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alista ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento.
# Seu programa também devará mostrar o tempo que falta ou que passou do prazo.
idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Ainda está cedo para se alistar, volta daqui {} anos'.format(18 - idade))
elif idade == 18:
    print('Meu jovem, aliste-se IMEDIATAMENTE!')
elif idade > 18:
    print('Agora não tem como fugir, você está {} anos atrasado'.format(idade - 18))
print('Boa Sorte')


