n = int(input("Informe o valor de n: "))


if n <= 0:
    print("Por favor, insira um número positivo.")

else:
    inicio = 1.5

    for i in range(n):
        
        numero = inicio + (i * 0.5)
        
        if i == n - 1:
            print(f"{numero:.1f}")
        else:
            print(f"{numero:.1f}", end=" ")