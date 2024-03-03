"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

produtos = ('café da manhã', 0.8, "almoço", 1.8, "desjejum", 0.8, "janta", 1.8)
print("CARDÁPIO DO RU")
for p in produtos:
    if produtos.index(p) % 2 == 0:
        print(f"{p:.<23}R${produtos[produtos.index(p)+1]:.2f}")
