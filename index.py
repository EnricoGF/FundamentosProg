string = "oi, arroz, cachorro, gato"
palavra = "oi"

if palavra in string:
    print("sim")
else:
    print("nao")

###################

a= ""
a.capitalize() # Maiusculo na primeira letra da linha
a.upper()
a.lower()
a.tittle() # Maiusculo A Cada Espaço
a.swapcase() #Se é lower vira upper se é upper vira lower
a.strip() #Remove espaços no inicio e no final
a.replace("cachorro", "rato") # Troca "cachorro" por "rato"
a.split()
a.count("x") # Conta quantos "x" tem na string
a.rfind("rato") # Retorna o indice do primeiro "rato" encontrado na string
a.endswith(".py") # Retorna bool se termina com ".py"
