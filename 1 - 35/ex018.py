''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA COSTA '''

#Faça um programa que leia um ângulo e informe o seu respectivo seno, cosseno e tangente.

import math
angulo = float(input('Digite o ângulo que voçê deseja: '))
sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de {}° tem o seno de {:.2f}, cosseno de {:.2f}, e tangente de {:.2f}'.format(angulo,sin,cos,tan))