"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""
qtd_de_alunos = int(input('Quantos alunos serão cadastrados? '))
dados = [[0 for i in range(3)] for j in range(qtd_de_alunos)]

for i in range(qtd_de_alunos):
    for j in range(3):
        if j == 0:
            nome = input('Nome do aluno: ')
            dados[i][j] = nome
        else:
            nota = float(input('Nota do aluno: '))
            dados[i][j] = nota

for i in range(qtd_de_alunos):
    media = (dados[i][1] + dados[i][2]) / 2
    dados[i].append(media)

print("NOME           N1             N2             MEDIA")
for i in range(qtd_de_alunos):
    for j in range(4):
        if j == 3:
            print(dados[i][j], end='')
        else:
            print(f'{dados[i][j]:.<15}', end='')
    print()
