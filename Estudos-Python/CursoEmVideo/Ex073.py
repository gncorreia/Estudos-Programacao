# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depos mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros colocados são {times[:5]}')
print('-=' * 15)
print(f'Os últimos 4 colocados são {times[16:]} ')
print('-=' * 15)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'Chapecoense está na {times.index("Chapecoense")+1}ª posição')
# ou coloca desse jeito {len(times[8])}')
print('-=' * 15)

