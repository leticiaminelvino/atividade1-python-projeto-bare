"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

soma = contador = 0
numero = 0

while numero != 999:
    numero = int(input('Digite um número (999 para parar): '))
    
    if numero != 999:
        soma += numero
        contador += 1

print(f'Foram digitados {contador} números.')
print(f'A soma entre eles é: {soma}.')
