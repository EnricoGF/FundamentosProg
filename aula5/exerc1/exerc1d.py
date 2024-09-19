n = int(input("Insira um numero: \n"))
index = 1

for i in range(1, n + 1):
    index *= i

print(f"O fatorial de {n} é {index}")