"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
pessoas = []
pesos = []
while True:
    nome = input('Digite seu nome: ')
    pessoas.append(nome)
    peso = float(input('Digite seu peso: '))
    pesos.append(peso)
    resp = input('Deseja continuar? [S/N]')
    if resp not in 'Ss':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O mais pesado é {pessoas[pesos.index(max(pesos))]} com {max(pesos):.1f}kg')
print(f'O mais leve é {pessoas[pesos.index(min(pesos))]} com {min(pesos):.1f}kg')
