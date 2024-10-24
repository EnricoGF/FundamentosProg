a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

linhas = len(a)
colunas = len(a[0])
print(f"matriz a[{linhas}][{colunas}]")

elemento4 = a[1][0]

def matrizVazia():
    linhas = 2
    colunas = 4
    matriz= []

    for i in range(linhas):
        matriz.append([0] * colunas)

    for linha in matriz:
        print(linha)

def varreduraIndex():
    linhas = 5
    colunas = 5
    matriz2 = []

    for i in range(linhas):
        matriz2.append(list(range(colunas)))

    for linha in range(linhas):
        for coluna in range(colunas):
            print(matriz2[linha][coluna], end = " ")
        print()