"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
e quantas mulheres têm menos de 20 anos.
"""

soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_de_20 = 0

for i in range(1, 5):
    print(f'--- Pessoa {i} ---')
    nome = input('nome: ')
    idade = int(input('idade: '))
    sexo = input('sexo (M/F): ').upper()

    soma_idades += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1

media_idade = soma_idades / 4

print(f'\na média das idades é {media_idade:.1f} anos.')
print(f'o homem mais velho se chama {nome_homem_mais_velho} e tem {idade_homem_mais_velho} anos.')
print(f'{mulheres_menos_de_20} mulheres têm menos de 20 anos.')
