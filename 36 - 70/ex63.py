"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""

n = int(input('Digite o numero de termos: '))
termo1 = 0
termo2 = 1
print(f'{termo1} -> {termo2}', end='')

i = 3

while i <= n:
    termo3 = termo1 + termo2
    print(f' -> {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    i += 1

print(' -> FIM')
