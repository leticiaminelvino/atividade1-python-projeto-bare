"""Autores: ADONAY SOUZA FERREIRA
            ALINE DAFFINY FERREIRA GOMES
            LETÍCIA MINELVINO DA_COSTA
"""

# Faça um programa que leia altura e largura de uma parede e mostre na tela a dimensão, a área e
# quantidade em litros de tinta necessária para pintar.

largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metros: '))
print('A dimensão da parede é {:.0f}x{:.0f} e a área é de {}m².\n'
      'Para pintar a parede será nessário {} litros de tinta.'
      .format(largura, altura, largura * altura, (largura*altura/2), altura*altura))
