"""
Alunos: 
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercício 04:
Faça um programa que leia algo pelo teclado e mostre na tela todas as informações possíveis sobre ela:"""

dado = input('Insira um valor: ')
print('O tipo primitivo desse valor é:', type(dado))
print('O valor inserido é alfabético:', dado.isalpha())
print('O valor inserido é numério:', dado.isnumeric())
print('O valor inserido é alfanumério:', dado.isalnum())
print('O valor inserido é um dígito:', dado.isdigit())
print('O valor inserido é todo minúculo:', dado.islower())
print('O valor inserido é todo maiúsculo:', dado.isupper())
print('O valor inserido é capitalizado:', dado.istitle())
print('O valor inserido é printável:', dado.isprintable())
