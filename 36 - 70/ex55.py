"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
pesos = []
for i in range(1, 6):
    peso = float(input(f'Digite o peso da pessoa {i}: '))
    pesos.append(peso)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'\no maior peso lido foi {maior_peso}kg')
print(f'o menor peso lido foi {menor_peso}kg')
