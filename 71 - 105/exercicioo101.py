"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.
"""
import datetime


def voto(nsc):
    idade = datetime.date.today().year - nsc
    if idade < 16:
        return 'NÃO PODE VOTAR'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))
