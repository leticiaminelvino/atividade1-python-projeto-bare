"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(nums):
    maior_num = nums[0]
    for num in nums:
        if num > maior_num:
            maior_num = num
    return maior_num


lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    while True:
        confirma = input('Deseja continuar? [S/N] ')
        if confirma in 'SsNn':
            break
        print("ERRO! Digite apenas S ou N.")
    if confirma in 'Nn':
        break

print(f'O maior valor foi {maior(lista)}')
