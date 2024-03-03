"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

tupla = (int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')),
         int(input('digite um valor: ')), int(input('digite um valor: ')))
cont = 0
pares = 0

# letra A
for numero in tupla:
    if numero == 9:
        cont += 1
if cont == 1:
    print(f"O número 9 foi digitado {cont} vez")
else:
    print(f"O número 9 foi digitado {cont} vezes")

# letra B
if 3 in tupla:
    print(f"O número 3 foi digitado pela primeira vez na posição {tupla.index(3)}")
else:
    print("O número 3 não foi digitado")

# letra C
for numero in tupla:
    if numero % 2 == 0:
        pares  += 1
        print(f"{numero} é par")
if pares == 0:
    print("Não houve números pares")
