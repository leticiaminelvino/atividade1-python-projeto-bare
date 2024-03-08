''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA_COSTA '''

#Faça um programa que leia quantos reais uma pessoa tem na carteira e quantos dólares ela pode comprar.

troca = float(input('Quanto dinheiro você tem na cateira? R$ '))
print('Com R${:.2f} você pode comprar U${:.2f}'.format(troca, troca/4.96))