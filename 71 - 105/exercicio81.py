"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []

while True:
    try:
        n = int(input('Digite um valor: '))
    except (ValueError, TypeError):
        break
    if n not in lista:
        lista.append(n)

print(f"Foram digitados {len(lista)} valores")

lista.sort(reverse=True)
print(f"Lista: {lista}")

if 5 in lista:
    print("O valor 5 foi digitado")
else:
    print("O valor 5 não foi digitado")
