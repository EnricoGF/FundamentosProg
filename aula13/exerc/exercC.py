""" Calcular o PIB per capita de cada município pela fórmula: PIB per
capita = PIB em Milhões R$ / População * 106, e mostrar na tela o
nome do município e o PIB per capita com 2 casas decimais,
somente para os municípios com PIB per capita entre (inclusive)
R$40.000 e R$50.000. """

import csv

if __name__ == '__main__':

    arquivo = open("aula13\exerc\cidades.csv")
    leitor = csv.reader(arquivo)
    dados = list(leitor)

    for registro in dados[1:]:
        pib = float(registro[2])*10**6
        capita = int(registro[1])
        calc = pib/capita

        if 40000 <= calc and 50000 >= calc:
            casaDecimal = "%.2f" % (calc)
            print(registro[0],":", casaDecimal)

    arquivo.close()