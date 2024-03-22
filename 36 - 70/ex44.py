'''
Alunos:
ADONAY SOUZA FERREIRA
ALINE DAFFINY FERREIRA GOMES
LETÍCIA MINELVINO DA COSTA

Exercicio 044:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
'''
print('{:-^40}'.format(' Lojas Bemol '))

preco = float(input('Informe o preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO: 
[1] à vista dinheiro/cheque 
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Escolha uma opção? '))

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, preco-(preco*0.1)))
elif opcao == 2:
    print(('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, preco-(preco*0.05))))
elif opcao == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f}'.format(preco, preco/2))
elif opcao == 4:
    parcela = int(input('Vai querer parcelar em quantas vezes? '))
    print('Sua compra será parcelada em {} de R${:.2f} COM JUROS'.format(parcela, (preco/parcela)+(preco/parcela)*0.2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,preco+(preco*0.2)))
else:
    print('Opção de pagamento INVÁLIDA. Tente novamente.')
