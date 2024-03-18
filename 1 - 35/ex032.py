"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Insira um ano, se quiser analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if (2024 - ano) % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano digitado foi {}, é bissexto.'.format(ano))
else:
    print('O ano digitado foi {}, não é bissexto.'.format(ano))
