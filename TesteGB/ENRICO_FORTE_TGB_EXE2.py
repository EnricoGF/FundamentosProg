def main(matriz):
    matrizTransposta = []
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        matrizTransposta.append([0] * colunas)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matrizTransposta[i][j] = matriz[j][i]
            
    print(matrizTransposta)

if __name__ == '__main__':
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    main(matriz)