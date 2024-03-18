"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que peça um número e que forneça o dobro, o triplo e raiz quadrada desse número.

num = int(input('Informe um número: '))
print('O dobro de {} é {},\n o seu triplo é {}\n e a sua raiz quadrada é {:.2f}'
      .format(num, (num*2), (num*3), (num**(1/2))))
