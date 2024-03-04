"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[], [], []]
soma_pares = 0
soma_3coluna = 0

for i in range(3):
    for j in range(3):
        num = int(input(f'Digite o elemento {i+1},{j+1}: '))

        if num % 2 == 0:
            soma_pares += num
        if j == 2:
            soma_3coluna += num

        matriz[i].append(num)

for i in range(3):
    print('|', end="")
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end=" ")
    print('|')

print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_3coluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
