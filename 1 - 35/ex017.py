"""
Alunos: 
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 17:
Faça um programa que leia o comprimento do cateto oposto e adjacente de triângulo retângulo e informe
o valor da hipotenusa. """

from math import hypot
num = float(input('Informe o comprimento do cateto oposto: '))
num2 = (float(input('Informe o comprimento do cateto adjacente: ')))
hip = hypot(num,num2)
print('A hipotenusa desse triângulo retângulo é igual a {:.2f}'.format(hip))
