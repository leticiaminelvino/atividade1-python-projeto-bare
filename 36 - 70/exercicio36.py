"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 036:
Construa um  programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
salário do comprador e em quantos anos ele deseja quitar a dívida. A prestação não pode exceder 30% do salário ou
então será negado o empréstimo """

casa = float(input('Qual o valor da casa? '))
salario = float(input('Informe um salário: '))
quitar = float(input('Em quantos anos deseja quitar o empréstimo? '))
prestacao = casa/(quitar*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, quitar, prestacao))

if prestacao <= (salario*0.3):
    print('Empréstimo concedido')
else:
    print('Empréstimo negado')
