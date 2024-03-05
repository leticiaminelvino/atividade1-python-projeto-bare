"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
import random


def sorteia(lista):
    for i in range(5):
        n = random.randint(1, 10)
        lista.append(n)
    return lista


def soma_par(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma


lista_n = []
sorteia(lista_n)
print(lista_n)
print(f'A soma de todos os valores na lista é {soma_par(lista_n)}')
