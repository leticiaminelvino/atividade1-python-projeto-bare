"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo_atual = primeiro_termo
i = 0
total_de_termos = 0
mais_termos = 10

print('A progressão aritmética é: ')
while mais_termos != 0:
    total_de_termos += mais_termos
    while i <= total_de_termos:
        print(f'{termo_atual} -> ', end='')
        termo_atual += razao
        i += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos vc quer mostrar a mais? '))

print(f'\nProgressão aritmética finalizada com {total_de_termos} mostrados')
