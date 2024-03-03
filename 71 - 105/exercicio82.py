"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
pares = []
impares = []

while True:
    try:
        n = int(input('Digite um valor: '))
    except (ValueError, TypeError):
        break
    if n not in lista:
        lista.append(n)

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Lista completa: {lista}')
print(f'Os valores pares digitados: {pares}')
print(f'Os valores impares digitados: {impares}')