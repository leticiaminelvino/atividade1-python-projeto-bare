"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(jogador, gols):
    if jogador == '':
        jogador = '[não informado]'
    if gols == '':
        gols = '[não informado]'

    return f'O jogador {jogador} fez {gols} gols'


nome = input('Nome do jogador: ')
g = input('Quantidade de gols marcados: ')
print(ficha(nome, g))
