"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = []
for i in range(5):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)

print(f"O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}")
print(f"O menor valor digitado foi {min(lista) } na posição {lista.index(min(lista))}")
