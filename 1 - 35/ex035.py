"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
lado1 = float(input('Insira o tamanho da primeiro lado: '))
lado2 = float(input('Insira o tamanhodo segundo lado: '))
lado3 = float(input('Insira o tamanho do terceiro lado: '))

if r1 + r2 > r3 and r1 +r3 > r2 and r2 +r3> r1:
   print("Os lados informados acima formam um triângulo")
else:
    print("Os lados informados não formam um triângulo")
