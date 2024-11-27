import csv

arquivo = open("../aula13/aula/pessoas.csv")
leitor = csv.reader(arquivo)
dados = list(leitor)
print(f"Cabeçalho: {dados[0]}")
for registro in dados[1:]:
    print(f"Linha: {registro}")

arquivo.close()