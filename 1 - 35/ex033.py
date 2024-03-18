"""
Alunos: 
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 33:
Faça um programa que leia 3 números e mostre qual deles é o maior e qual o menor: """

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('Os números digitados foram: [{},{}, {}]'.format(n1, n2, n3))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
