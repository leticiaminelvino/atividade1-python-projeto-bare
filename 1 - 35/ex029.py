"""
Alunos: 
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 29:
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km, mostre uma mensagem que ele
foi multado. A multra vai custar R$7,00 a cada  Km acima do limite. """

vel = int(input('Informe a velocidade do veículo: '))
multa = (vel - 80)*7
if vel > 80:
    print('Veículo multado em R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
