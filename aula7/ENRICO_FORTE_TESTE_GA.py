import os

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    opcao = input("Escolha uma opção:\n1 - Iniciar a bipagem dos produtos.\n2 - Escolher método de pagamento\n3 - Mostrar valor a ser pago\nX - Fechar\n").upper()
    return opcao

def iniciar():
    quantProd = int(input("Quantos produtos deseja comprar? "))
    valTotal = 0

    for i in range(0, quantProd):
        input("Digite o nome do produto: ")
        valProd = float(input("Digite o valor do produto: "))
        valTotal += valProd
        i+=1
    return valTotal

def escolher():
    pergunta = "Digite C para pagar por crédito, D para débito ou P para PIX: "
    metodPagmto = None

    while metodPagmto != "C" and metodPagmto != "D" and metodPagmto != "P":
        metodPagmto = input(pergunta).upper()
    return metodPagmto

def mostrar(pagamento, valorProd):
    if valorProd == None:
        print("O valor total ainda não foi definido. Retorne para opção 1.")
    elif pagamento == "C":
        print(f"Valor com taxas: {valorProd + ((valorProd / 100) * 3.19)}")
    elif pagamento == "D":
        print(f"Valor total da compra: {valorProd}")
    elif pagamento == "P":
        print(f"Valor total com desconto: {valorProd - (valorProd * 0.02)}")
    else:
        print("O método de pagamento ainda não foi inserido. Retorne para a opção 2.")    
    
def fechar():
    print("Obrigado pela preferência.")
    exit()

if __name__ == '__main__':
    opcao = 0
    metodoPagamento = None
    valorProdutos = None

    while opcao != "X":
        opcao = menu()
        match opcao:
            case "1":
                valorProdutos = iniciar()
            case "2":
                metodoPagamento = escolher()
            case "3":
                mostrar(metodoPagamento, valorProdutos)
            case "X":
                fechar()
            case _:
                print("Opção inválida.")

        input("\nPressione ENTER para continuar...")
        opcao = 0