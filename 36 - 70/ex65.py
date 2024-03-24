"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
continuar = 'S'
soma = contador = 0

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1

    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]

print(f'Você digitou {contador} numeros e a média foi {soma/contador}')
print(f'o maior valor foi {maior} e o menor foi {menor}')
