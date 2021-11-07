# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Fortaleza', 'Corinthians', 'Internacional', 'Fluminense',\
        'Cuiabá', 'América-MG', 'Atlético-GO', 'Sao Paulo', 'Ceará SC', 'Atlético-PR', 'Santos', 'Bahia', 'Sport Recife',\
        'Juventude', 'Grêmio', 'Chapecoense'
print(f'Os cinco primeiros colocados são: {times[:5]}')
print(f'Os quatro ultimos colocados são {times[16:]}')
print(f'Times no Brasileirão 2021\n{sorted(times)}')
print(f'A Chapecoense está na posição {times.index("Chapecoense") + 1}')