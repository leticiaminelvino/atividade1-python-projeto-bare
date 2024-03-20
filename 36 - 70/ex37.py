"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input('Digite um numero inteiro: '))
conversao = int(input('Escolha para qual base você deseja converter esse número:\n 1 - binário\n 2 - octal \n 3 - hexadecimal: \n'))

if conversao == 1:
    print(f'\n{num} convertido para binário é {bin(num).replace("0b", "") }')
elif conversao == 2:
    print(f'\n{num} convertido para octal é {oct(num).replace("0o", "") }')
elif conversao == 3:
    print(f'\n{num} convertido para hexadecimal é {hex(num).replace("0x", "") }')
else:
    print('opcao invalida')
