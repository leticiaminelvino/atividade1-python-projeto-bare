"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que leia o nome de 4 alunos e sorteie aleatoriamente 1 deles.

import random
n1 = input('Nome aluno 1: ')
n2 = input('Nome aluno 2: ')
n3 = input('Nome aluno 3: ')
n4 = input('Nome aluno 4: ')
lista = [n1,n2, n3, n4]
sorteio = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteio))
