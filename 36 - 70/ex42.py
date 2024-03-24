"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

print('{:-^40}'.format(' Analisador de Triângulos '))

a = float(input('Digite o primeiro segmento de reta: '))
b = float(input('Digite o segundo segmento de reta: '))
c = float(input('Digite o terceiro segmento de reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
