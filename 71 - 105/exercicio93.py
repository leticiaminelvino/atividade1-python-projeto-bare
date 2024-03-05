"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai
ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
partidas = []

jogador['nome'] = input('Nome do jogador: ')
total = int(input('Quantas partidas ele jogou? '))

for i in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {i+1}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
