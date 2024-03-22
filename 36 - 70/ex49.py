'''
Alunos:
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 049:
Refaça o desafio 09 mostrando a tabuada de um número que o usuário escolher, utilizando um laço FOR.
'''

tab = int(input('Insira um número para ver sua tabuada: '))
for num in range (1,11):
    print('{} x {:2} = {}'.format(tab, num, tab*num))
