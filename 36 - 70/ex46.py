'''
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 046:
Crie um programa que mostre na tela uma contagem regressiva para estouro de fogos de
de artifício, indo de 10 até 0, com pausa de 1 segundo entre elas.
'''
from time import sleep
for contagem in range (10,-1,-1):
    print(contagem)
    sleep(1)
print('''BUM!
  BUM!
     POW!
        FELIZ ANO NOVO !''')
