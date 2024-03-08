''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA_COSTA '''

#Faça um programa que leia o salário do funcionário e informe o salario antes e apos o reajuste com adicional de 15%

salario = float(input('Infome o salário do funcionário: R$ '))
print('O funcionário que ganhava R$ {:.2f}, com reajuste de 15%, receberá R${:.2f}'.format(salario, salario+(salario*0.15)))