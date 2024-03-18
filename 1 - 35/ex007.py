"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que peça duas notas de um aluno e mostre a média com duas casas decimais.

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
print('A média entre {:.1f} e {:.1f} é igual a {:.2f}'.format(n1, n2, (n1+n2)/2))
