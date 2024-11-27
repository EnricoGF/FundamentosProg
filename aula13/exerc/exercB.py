""" Mostre na tela o nome e a população dos municípios que possuem
menos que 22000 ou mais que 41000 habitantes """

import csv

if __name__ == '__main__':

    arquivo = open("aula13\exerc\cidades.csv")
    leitor = csv.reader(arquivo)
    dados = list(leitor)

    for registro in dados[1:]:
        if int(registro[1]) < 22000 or int(registro[1]) > 41000:
            print(registro[0], ":", registro[1])

    arquivo.close()