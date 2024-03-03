"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
import random

num = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
       random.randint(0,100), random.randint(0, 100))

print(f"valores na tupla: {num}")
print(f"o menor valor é {min(num)}")
print(f"o maior valor é {max(num)}")