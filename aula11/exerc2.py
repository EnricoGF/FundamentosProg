def encontrarIndice(vetor, numero):
    for indice, valor in enumerate(vetor):
        if valor == numero:
            return indice
    return -1

def main():
    lista = []
    tamanho = int(input("Insira o tamanho da sua lista: "))

    while len(lista) < tamanho:
        lista.append(int(input("Insira um número inteiro: ")))

    numero = int(input("Insira um número para pesquisar no vetor: "))

    indice = encontrarIndice(lista, numero)
    
    if indice != -1:
        print(f"O número {numero} foi encontrado no índice {indice}.")
    else:
        print(f"O número {numero} não foi encontrado no vetor.")

if __name__ == "__main__":
    main()
