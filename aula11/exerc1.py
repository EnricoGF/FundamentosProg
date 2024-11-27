def qtdNegativos(list):
    cont = 0

    for i in range(len(list)):
        if list[i] < 0:
            cont += 1
    
    return cont

def array():
    lista = []
    tamanho = int(input("Insira o tamanho da sua lista: "))

    while len(lista) < tamanho:
        lista.append(int(input("Insira um número inteiro: ")))

    return lista

if __name__ == '__main__':
    lista = array()
    quantidade = qtdNegativos(lista)

    print(f"A quantidade de valores negativos na lista {lista} é: {quantidade}")