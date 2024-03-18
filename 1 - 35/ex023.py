"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que leia um número e informe qual é a unidade, a dezena, a dentena e o milhar.

num = int(input('Insira um valor: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número', num)
print('unidade:', u)
print('Dezena:', d)
print('Centena:', c)
print('Milhar:', m)
