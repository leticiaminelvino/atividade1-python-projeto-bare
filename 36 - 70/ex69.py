"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

pessoas_mais_dezoito = 0
homens_cadastrados = 0
mulheres_menos_vinte = 0

while True:
    print('{:-^40}'.format('CADASTRE UMA PESSOA'))

    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip().upper()

    if idade >= 18:
        pessoas_mais_dezoito += 1

    if sexo == 'M':
        homens_cadastrados += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar != 'S':
        break

print('{:-^40}'.format('RESULTADO DO CADASTRO'))

print(f'Total de pessoas com mais de 18 anos: {pessoas_mais_dezoito}')
print(f'Total de homens cadastrados: {homens_cadastrados}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos_vinte}')
