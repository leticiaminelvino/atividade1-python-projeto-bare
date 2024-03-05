"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""


def contador(i, f, p):
    num = i
    if i < f:
        while num <= f:
            print(num, end=" ")
            num += p
    else:
        while num >= f:
            print(num, end=" ")
            num += -p


print('QUESTÃO A')
contador(1, 10, 1)

print('\nQUESTÃO B')
contador(10, 0, 2)

print('\nQUESTÃO C')
contador(int(input('Informe um ínicio: ')),
         int(input('Informe um fim (irá parar um passo antes): ')),
         int(input('Informe o passo: ')))
