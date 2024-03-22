"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 050: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0

for i in range(6):
    num = int(input("digite um número inteiro: "))
    if num % 2 == 0:
        soma += num

print("a soma dos pares é:", soma)
