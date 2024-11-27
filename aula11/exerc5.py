matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        linha.append(i + j / 10)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:.1f}", end=" ")
    print()

print("\nDiagonal secundária:")
cont1 = 0
cont2 = 9
while cont1 < 10:
    print(matriz[cont1][cont2])

    cont1 += 1
    cont2 -= 1