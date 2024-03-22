'''
Alunos:
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 070:
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total de gastos na compra.
b) Quantos produtos custam mais de 1000 reais.
c) Qual é o nome do produto mais barato.
'''
total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Quanto custa: R$ '))
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Compra finalizada')
print(f'Total da compra foi R${total:.2f}')
print(f'{totmil} produtos custam mais de R$1000.00')
print(f'O produto mais barato custa R${menor:.2f}')
