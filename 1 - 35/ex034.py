''' Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA COSTA '''

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
# Para salários superiores a R$1250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário atual do funcionário: '))

if salario >1250:
   novo_salario = salario + (salario*0.1)
if salario <= 1250:
   novo_salario = salario + (salario*0.15)
print('O salário do funcionário era de R${:.2f}.\n O novo salário é de R${:.2f}'.format(salario , novo_salario))