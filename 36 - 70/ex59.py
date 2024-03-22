"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa

Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))

while True:
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair do programa")

    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        resultado = num1 + num2
        print(f"a soma de {num1} e {num2} é igual a {resultado}")
    elif opcao == 2:
        resultado = num1 * num2
        print(f"a multiplicação de {num1} e {num2} é igual a {resultado}")
    elif opcao == 3:
        if num1 > num2:
            print(f"o maior número é {num1}")
        elif num2 > num1:
            print(f"o maior número é {num2}")
        else:
            print("os números são iguais")
    elif opcao == 4:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
    elif opcao == 5:
        print("programa encerrado")
        break
    else:
        print("opção inválida. por favor, escolha uma opção válida")
