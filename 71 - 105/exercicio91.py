"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado
"""
import random

jogadas = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6),
           'jogador3': random.randint(1, 6), 'jogador4': random.randint(1, 6)}

for i in sorted(jogadas, key=jogadas.get):
    print(f'{i} tirou {jogadas[i]}')
