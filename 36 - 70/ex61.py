"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo_atual = primeiro_termo
i = 0

print('A progressão aritmética é: ', end='')
while i < 10:
    print(f'{termo_atual} -> ', end='')
    termo_atual += razao
    i += 1

print('FIM')
