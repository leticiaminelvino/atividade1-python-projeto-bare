''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA COSTA '''

#Faça um programa que leia um nome completo e mostre uma frase de cumprimento, o primeiro e o último nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))