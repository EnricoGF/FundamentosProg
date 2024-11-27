# open("index.py", "r") # name, mode
# name: nome com local do arquivo
# mode: 
# "r" leitura a partir do inicio
# "w" escrita (se o arquivo existir terá o conteudo apagado)
# "x" exclusivo para criação de arquivo (falha se ja existe)
# "a" leitura a partir do final
# "t" texto
# "b" binário (rb, wb, ab, rb+)
# "+" indica leitura e escrita (r+, a+)

""" arquivo = open("texto.txt", "w")
arquivo.write("Acessando arquivos\ncom Python")
arquivo.close()

arquivo = open("texto.txt", "r")
print(arquivo.read())
arquivo.close()
 """


# retorna uma lista com cada linha do arquivo 
""" arquivo = open("texto.txt", "r")
arquivo.write("dadada")
texto = arquivo.readlines()
arquivo.close()
print(texto) """


# escreve linhas no arquivo
""" lista = ["cachorro\n", "gato\n"]

arquivo = open("texto.txt", "r")
texto = arquivo.writelines(lista)
arquivo.close()
print(texto) """


# n precisa fechar arquivo
""" with open("pessoas.csv") as f:
    f.write("Primeira linha")
    f.write("Segunda Linha") """
