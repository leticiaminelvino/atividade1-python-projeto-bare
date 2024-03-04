"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        num = int(input(f'Digite o elemento {i},{j}: '))
        matriz[i].append(num)

for i in range(3):
    print('|', end="")
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end=" ")
    print('|')
