''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA COSTA '''

#Faça um programa que peça um número real qualquer e informe o número digitado e a sua parte inteira.

from math import floor
num = float(input('Digite um um número real: '))
inteiro = floor(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, inteiro))
