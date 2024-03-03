"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 079:  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

lista = []

while True:
    try:
        n = int(input('Digite um valor: '))
    except (ValueError, TypeError):
        break
    if n not in lista:
        lista.append(n)

print(f'Os valores digitados foram: {sorted(lista)}')
