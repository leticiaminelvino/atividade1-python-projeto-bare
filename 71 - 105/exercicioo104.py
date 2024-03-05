"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""


def leia_int(inpt):
    try:
        n = int(inpt)
        return n
    except ValueError:
        print('\033[31mERRO! Função leia_int() aceita somente inteiros')
        quit()    # se não for inteiro, o programa é encerrado aqui mesmo


var = leia_int(input('leia_int('))
print(var)
print(var+1)
