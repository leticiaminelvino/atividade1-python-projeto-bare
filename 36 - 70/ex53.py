"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 053: Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando os espaços.
"""

def eh_palindromo(frase):
    frase_sem_espacos = frase.replace(" ", "").lower()
    return frase_sem_espacos == frase_sem_espacos[::-1]

frase = input("digite uma frase: ")

frase_invertida = frase[::-1]
print("frase invertida:", frase_invertida)

if eh_palindromo(frase):
    print("é um palíndromo")
else:
    print("não é um palíndromo")
