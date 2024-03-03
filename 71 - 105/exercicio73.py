"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

ranking = ("Palmeiras", "Grêmio", "Atlético Mineiro", "Flamengo", "Botafogo", "Bragantino", "Fluminensee",
           "Atlético Parananense", "Internacional", "Fortaleza", "São Paulo", "Cuiabá", "Corinthians",
           "Cruzeiro", "Vasco", "Bahia", "Santos", "Goiás", "Coritiba", "Chapecoense")
times = []
for time in ranking:
    times.append(time)
times.sort()

print(f"OS 5 PRIMEIROS COLOCADOS: {ranking[0:5]}")
print(f"OS 4 ÚLTIMOS COLOCADOS: {ranking[-4:]}")
print(f"Os times em ordem alfabética: {times}")
print(f"Chapecoense está em {ranking.index("Chapecoense")+1}° lugar")
