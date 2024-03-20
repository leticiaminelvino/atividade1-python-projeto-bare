"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print('Você deve se alistar esse ano')
else:
    print(f'Você está {idade - 18} anos atrasado para o seu alistamento.')
