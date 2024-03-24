"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 052: Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
"""

num = int(input("Digite um numero: "))
total=0
for i in range(1, num + 1):
    if num % i == 0:
        print("\033[32m", end='')
        total+=1
    else:
        print("\033[31m", end='')
    print(f'{i} ', end='')
print(f'\n\033[mO numero {num} foi divisivel {total} vezes')
if total == 2:
    print('E por isso ele eh PRIMO')
else:
    print('E por isso ele NÃO EH PRIMO')
  
