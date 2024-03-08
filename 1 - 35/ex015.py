''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA_COSTA '''

#Faça um programa que pergunte a quantidade de dias percorridos e km rodados por um carro alugado. Infome o preço a pagar
#sabendo que R$60/dia e R$0.15/km rodado.

dia =float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
print('O valor total a pagar é de R${:.2f}'.format(dia*60+0.15*km))
