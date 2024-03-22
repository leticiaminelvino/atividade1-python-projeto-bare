"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
"""

sexo = 'inicializando variavel'
while sexo not in 'MmFf':
    sexo = input('Digite o sexo (M/F): ').upper()
  
print('sexo registrado:', sexo)
