"""
Alunos: 
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 22:
Faça um programa que peça o nome completo de uma pessoa e informe o nome todo em maiusculo, minusculo,
o primeiro nome e quantas letras no primeiro nome. """

nome = str(input('Insira seu nome completo: ')).strip()
print('Seu nome em maiúsculas é:', nome.upper())
print('Seu nome em minúsculas é: ', nome.lower())
print('Seu nome tem ao todo:', len(nome) - nome.count(' '))
nome = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome[0], len(nome[0])))
