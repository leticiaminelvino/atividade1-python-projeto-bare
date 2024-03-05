"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    if num == 1 or num == 0:
        return 1
    if show:
        print(f'{num} x {fatorial(num - 1, True)} = {num * fatorial(num - 1)}')
    return num * fatorial(num - 1)


n = int(input('Digite um numero para calcular o fatorial: '))
while True:
    visual = input('Deseja visualizar o processo? [S/N] ')
    if visual in 'SsNn':
        if visual in 'Ss':
            visual = True
        else:
            visual = False
        break
    else:
        print('ERRO! Digite apenas S ou N.')

print(fatorial(n, visual))
