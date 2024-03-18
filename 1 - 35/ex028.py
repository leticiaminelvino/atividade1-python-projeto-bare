"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""
# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá informar se o usuário venceu ou perdeu.

import random
num = int(input('Digite um número entre 0 e 5: '))
lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)
print(sorteio)

if num == sorteio:
    print('Match, você acertou')
else:
    print('Ops, tente novamente')
