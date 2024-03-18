"""
Alunos: 
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 31:
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas. """

dist = int(input('Infome a distância da viagem: '))
preço1 = dist*0.50
preço2 = dist*0.45
if dist <= 200:
    print('Você está prestes a começar uma viagem de {}.'.format(dist))
    print('O preço da passagem custa R$ {}'.format(preço1))
if dist > 200:
    print('Você está prestes a começar uma viagem de {}.'.format(dist))
    print('O preço da passagem custa R$ {}'.format(preço2))
