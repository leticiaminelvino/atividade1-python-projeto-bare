"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que leia uma frase e mostre quantas vezes aparece a letra 'A',
# em que posição a letra 'A' aparece pela primeira e última vez.

frase = (input('Digite uma frase: ')).strip()
print('A letra a aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra a apareceu na posição {}'.format(frase.upper().find('A')))
print('A última letra a apareceu na posição {}'.format(frase.upper().rfind('A')))
