"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print('{:-^40}'.format('JOGO DE PAR OU ÍMPAR'))

vitorias_consecutivas = 0

while True:
    jogador = int(input('Digite um número: '))
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()

    computador = randint(0, 10)

    soma = jogador + computador
    resultado = 'P' if soma % 2 == 0 else 'I'

    print(f'Você jogou {jogador} e o computador jogou {computador}. {soma} é {resultado}')

    if resultado == escolha:
        print('Você venceu!')
        vitorias_consecutivas += 1
    else:
        print('Você perdeu')
        break

print('-' * 30)
print(f'Total de vitórias consecutivas: {vitorias_consecutivas}')
