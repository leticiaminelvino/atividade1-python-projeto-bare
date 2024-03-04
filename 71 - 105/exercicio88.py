"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
"""
import random

qtd = int(input('Quantos palpites deseja gerar? '))
palpites = [[0 for i in range(6)] for j in range(qtd)]

print("\nGERANDO PALPITES...")
for i in range(qtd):
    for j in range(6):
        palpites[i][j] = random.randint(1, 60)
    print(palpites[i])