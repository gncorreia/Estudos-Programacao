# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ''SANTO''

cidade = str(input(('Digite o nome de uma cidade: ')).strip())
#formatado = cidade[:5].upper() == 'SANTO'
print('A cidade {} começa com santo? {}'.format(cidade, cidade[:5].upper() == 'SANTO'))





# == (igualdade)
# sempre pense se o usuário vai fazer besteira na hora de usar