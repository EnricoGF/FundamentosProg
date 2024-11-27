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

print("\nDiagonal principal:")
for i in range(0, 10):
    print(matriz[i][i])