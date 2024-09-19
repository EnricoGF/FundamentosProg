tamanho = int(input("Insira o tamanho: "))
ast = "*"
esp = " "

for i in range(tamanho, 0, -1):  # i vai de 5 até 1, decrementando de 1 em 1
    for j in range(i):
        print(ast, end = esp)
    print()