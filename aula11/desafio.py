n = int(input("Informe um número entre 3 e 15: "))
while n < 3 or n > 15:
    n = int(input("Número inválido! Informe um número entre 3 e 15: "))

meio = n // 2
for i in range(n):
    for j in range(n):
        if abs(i - meio) + abs(j - meio) == meio:
            print("X", end=" ")
        else:
            print("-", end=" ")
    print()
#numero par buga