"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que leia a cidade de nascimento ignorando os espaços e se ela começar com
# 'Santo' indicar 'True'

cidade = str(input('Em que cidade você nasceu: ')).strip()
print(cidade.upper()[:5] == 'SANTO')
