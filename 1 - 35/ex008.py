''' Autores: ADONAY SOUZA FERREIRA \
            ALINE DAFFINY FERREIRA GOMES \
            LETÍCIA MINELVINO DA_COSTA '''

#Faça um programa para inserir a distância em metros e que forneça o valor correspondente em km, hm, dam, dm, cm , mm

d = float(input('Insira o valor da distancia em metros: ',))
print('A medida de {} metros corresponde a: \n {} km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(d, (d/1000), (d/100), (d/10), (d*10), (d*100), (d*1000) ))