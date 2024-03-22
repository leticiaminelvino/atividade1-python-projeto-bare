'''
Alunos:
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 048:
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
e que se encontram no intervalo de 1 até 500.
'''
soma = 0
for num in range (1,501,2):
    if num % 3 == 0:
        soma = soma + num
print('A soma de todos os números solicitados é: {}'.format(soma))
