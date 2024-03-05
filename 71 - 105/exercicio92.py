"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
import datetime
ano = datetime.date.today().year

dados = dict()
dados['Nome'] = input('Digite seu nome: ')
nascimento = int(input('Digite o ano de nascimento: '))
dados['Idade'] = ano - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (digite 0 se não possui): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Qual o ano de contratação: '))
    dados['Salário'] = float(input('Digite o salário: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - ano)

for k, v in dados.items():
    print(f'{k}: {v}')
