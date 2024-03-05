"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

dados = {'nome': input('NOME DO ALUNO: '), 'nota': float(input('NOTA DA PROVA: '))}
print(f'O aluno {dados["nome"]} tirou {dados["nota"]} na prova')
