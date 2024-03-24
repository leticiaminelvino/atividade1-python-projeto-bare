"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. 
"""

while True:
    numero = int(input('Digite um número para ver sua tabuada [digite um número negativo para encerrar o programa]: '))

    if numero < 0:
        print('Programa encerrado.')
        break

    print('-' * 30)
    print(f'Tabuada do {numero}')
    print('-' * 30)

    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
