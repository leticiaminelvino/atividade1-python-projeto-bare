''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA_COSTA '''

# Faça um programa que peça o valor da temperatura em °C e converta em °F.

celsius = float(input('Infome a temperatura em graus Celsius: '))
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(celsius, (celsius*1.8)+32))