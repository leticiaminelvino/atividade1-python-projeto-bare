"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogador = dict()
time = []
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    total = int(input('Quantas partidas ele jogou? '))

    partidas.clear()
    for i in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {i+1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        confirma = input('Deseja continuar? [S/N] ').upper()[0]
        if confirma in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if confirma == 'N':
        break

while True:
    busca = int(input('qual jogador deseja ver? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print('ERRO! Esse jogador não existe')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]['nome']}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'Na partida {i+1}, fez {g} gols')
