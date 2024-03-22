'''
Alunos:
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 045:
Crie um programa que faça o computador jogar Jokenpô com você.
'''
print('{:-^40}'.format(' Jokenpô '))

from random import randint
from time import sleep
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
jogador = int(input('''SUAS OPÇÕES:
[0] PEDRA 
[1] PAPEL
[2] TESOURA 
Qual é a sua jogada? '''))
print ('JO')
sleep(1)
print(' KEN')
sleep(1)
print('  PÔ!')
print('{:-^40}'.format(''))

if jogador == 0:
    print('Sua jogada foi PEDRA')
elif jogador == 1:
    print('Sua jogada foi PAPEL')
elif jogador == 2:
    print('Sua jogada foi TESOURA')
else:
    print('Jogada inválida')
print('O computador jogou {}'.format(lista[computador]))
print('{:-^40}'.format(''))

if computador == jogador:
    print('EMPATE')
elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0:
    print('Jogador venceu')
elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
    print('Computador venceu')
else:
    print('Informe um número válido, tente novamente!')
