from datetime import date

menores_idade = 0
maiores_idade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da pessoa {i}: '))
    idade = date.today().year - ano_nascimento
    if idade < 18:
        menores_idade += 1
    else:
        maiores_idade += 1

print(f'\nPessoas menores de idade: {menores_idade}')
print(f'Pessoas maiores de idade: {maiores_idade}')
