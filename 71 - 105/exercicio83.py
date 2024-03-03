"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = input('Digite uma expressão matemática que use parênteses: ')
parenteses = []

for char in expressao:
    if char == "(":
        parenteses.append("(")
    elif char == ")":
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(")")
            break

if len(parenteses) == 0:
    print("Tudo certo")
else:
    print("Erro na digitação")