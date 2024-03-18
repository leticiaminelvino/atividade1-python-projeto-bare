"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
lado1 = float(input('Insira o tamanho da primeiro lado: '))
lado2 = float(input('Insira o tamanhodo segundo lado: '))
lado3 = float(input('Insira o tamanho do terceiro lado: '))
forma = False

if lado1 + lado2 > lado3:
    forma = True
if lado1 + lado3 > lado2:
    forma = True
if lado2 + lado3 > lado1:
    forma = True
else:
    print(False)
print('Os lados informados formam um triângulo? {}'.format(forma))
