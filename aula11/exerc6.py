matriz= []

for i in range(10):
    matriz.append(list("-" * 10))

for i in range(0, 10):
    matriz[i][i] = "X"

cont1 = 0
cont2 = 9
while cont1 < 10:
    matriz[cont1][cont2] = "X"

    cont1 += 1
    cont2 -= 1

for linha in matriz:
    for coluna in linha:
        print(coluna, end=" ")
    print()