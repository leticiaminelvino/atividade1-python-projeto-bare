''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA_COSTA '''

#Faça um programa que peça o valor do produto e mostre na tela o valor do produto antes e depois do desconto de 5%.

preço = float(input('Insira o valor do produto: R$ '))
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai passar a custar R${:.2f}.'.format(preço, preço-(preço*0.05)))