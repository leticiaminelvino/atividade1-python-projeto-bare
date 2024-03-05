"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(largura, comprimento):
    return largura * comprimento


L = float(input('Largura do terreno em metros: '))
C = float(input('Comprimento do terreno em metros: '))
print(f'a area do terreno é {area(L, C)}m^2')
