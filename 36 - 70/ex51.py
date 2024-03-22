"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro_termo = int(input("digite o primeiro termo da PA: "))
razao = int(input("digite a razão da PA: "))

print("os 10 primeiros termos da progressão aritmética são:")

for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" -> ")
print("fim")
