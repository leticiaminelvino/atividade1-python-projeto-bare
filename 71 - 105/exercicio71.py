"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

notas_50 = 0
notas_20 = 0
notas_10 = 0
moedas_1 = 0
valor_a_sacar = float(input("QUAL VALOR DESEJA SACAR?     R$"))
print(f"\nSACANDO R${valor_a_sacar:.2f}...")

if valor_a_sacar >= 50:
    notas_50 = valor_a_sacar // 50
    valor_a_sacar -= (notas_50 * 50)

if valor_a_sacar >= 20:
    notas_20 = valor_a_sacar // 20
    valor_a_sacar -= (notas_20 * 20)

if valor_a_sacar >= 10:
    notas_10 = valor_a_sacar // 10
    valor_a_sacar -= (notas_10 * 10)

if valor_a_sacar >= 1:
    moedas_1 = valor_a_sacar // 1
    valor_a_sacar -= moedas_1

# PRINT
if notas_50 > 0:
    print(f"{notas_50:.0f} NOTAS DE R$50")
if notas_20 > 0:
    print(f"{notas_20:.0f} NOTAS DE R$20")
if notas_10 > 0:
    print(f"{notas_10:.0f} NOTAS DE R$10")
if moedas_1 > 0:
    print(f"{moedas_1:.0f} MOEDAS DE R$1")
if valor_a_sacar > 0:
    print(f"R${valor_a_sacar:.2f} IMPOSSÍVEIS DE SACAR")
