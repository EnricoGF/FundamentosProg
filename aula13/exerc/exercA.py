""" Mostre na tela somente o nome dos municípios que não possuem nome composto; """

import csv

if __name__ == '__main__':
    cont = 0

    arquivo = open("aula13\exerc\cidades.csv")
    leitor = csv.reader(arquivo)
    dados = list(leitor)

    for registro in dados[1:]:
        cont = registro[0].count(" ")
        
        if cont == 0:
                print(registro[0])

    arquivo.close()