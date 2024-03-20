"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 036:
Construa um  programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
salário do comprador e em quantos anos ele deseja quitar a dívida. A prestação não pode exceder 30% do salário ou
então será negado o empréstimo """

print('bem vindo ao seu banco de empréstimos')
valor_da_casa = float(input('por favor, informe o valor da casa que você quer comprar: '))
salario_da_pessoa = float(input('por favor, informe o seu salário mensal: '))
anos_a_pagar_casa = int(input('por favor, informe em quantos anos você pretende pagar a casa: '))

num_minimo_prestacoes = valor_da_casa / (anos_a_pagar_casa * 12)

if num_minimo_prestacoes > ((salario_da_pessoa * 0.3)):
    print(f'empréstimo negado, as prestações passam 30% do seu salário')
else:
    print(f'empréstimo aceito, você deve pagar R$ {num_minimo_prestacoes:.2f} mensalmente por {anos_a_pagar_casa * 12} meses')






