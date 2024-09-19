tamanho = int(input("Insira o tamanho: "))
ast = "*"
esp = " "

for i in range(1, tamanho + 1):
    for j in range(i):
        print(ast, end = esp)  # imprime o asterisco e fica na mesma linha
    print()