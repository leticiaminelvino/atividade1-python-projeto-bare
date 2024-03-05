"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

galera = list()
pessoa = dict()
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('digite seu nome: ')
    while True:
        pessoa['sexo'] = input('digite seu sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F.')

    pessoa['idade'] = int(input('digite sua idade: '))

    galera.append(pessoa.copy())

    while True:
        confirma = input('Deseja continuar? [S/N] ').upper()[0]
        if confirma in 'SN':
            break
        print('ERRO! digite apenas S ou N.')
    if confirma == 'N':
        break

print(f'{len(galera)} pessoas foram cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:.2f} anos.')
print('Mulheres cadastradas:')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
print('Lista de pessoas acima da media de idade:')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}')
