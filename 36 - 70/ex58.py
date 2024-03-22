"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costab

Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

"""
import random

print('oiieeee pensei em um número entre 0 e 10, tenta adivinhar')
numero = random.randint(0, 10)
tentativas = 0

while True:
    palpite = int(input('qual seu palpite? '))
    tentativas += 1

    if palpite == numero:
        print(f'AEEEEEEEEE! vc acertou em {tentativas} tentativas')
        break
    elif palpite < numero:
        print('um maior, de novo')
    else:
        print('um menor, de novo')
