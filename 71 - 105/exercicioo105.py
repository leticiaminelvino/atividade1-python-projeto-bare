"""
ALUNOS:
Adonay Souza Ferreira
Aline Daffiny Ferreira Gomes
Leticia Minelvino da Costa


5: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""


def notas(*n, situacao=False):
    """
    OBEJTIVO: ORGANIZAR DADOS DE ALUNOS
    :param n: notas dos alunos
    :param situacao: status do aluno (opcional)
    :return: dicionario com os dados organizados
    """
    d = dict()
    d['total de notas'] = len(n)
    d['maior nota'] = max(n)
    d['menor nota'] = min(n)
    d['media'] = sum(n)/len(n)

    if situacao:
        if d['media'] >= 8:
            d['situacao'] = 'ÓTIMO'
        elif 6 <= d['media'] < 8:
            d['situacao'] = 'OK'
        else:
            d['situacao'] = 'RUIM'

    return d


# main
help(notas)

consulta = notas(10, 7.5, 9, 9.5, situacao=True)
print(consulta)
