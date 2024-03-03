"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ("bioinformatica", "programar", "bemol", "python", "bare")
vogais = ("a", "e", "i", "o", "u")

for palavra in palavras:
    print(palavra, end=", vogais: ")
    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")
    print()
