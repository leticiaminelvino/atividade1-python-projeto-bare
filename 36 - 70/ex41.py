"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o 
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = 2024 - ano_nascimento

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'O atleta tem {idade} anos e está na categoria {categoria}')
