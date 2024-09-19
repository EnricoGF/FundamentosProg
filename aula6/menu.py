import time
import os

def menu():
    os.system("cls" if os.name == "nt" else "clear")

    print("\nDesenvolvendo um menu\n\n1) Opção 1\n2) Opção 2\n3) Opção 3\n9) Sair")
    opcao = int(input("Esolha uma opção: "))
    return opcao

def opcao1():
    print("opcao 1")

def opcao2():
    print("opcao 2")

def opcao3():
    print("opcao 3")

if __name__ == '__main__':
    escolha = 0

    while escolha != 9:
        escolha = menu()

        if escolha == 1:
            opcao1()
        elif escolha == 2:
            opcao2()
        elif escolha == 3:
            opcao3()
        elif escolha == 9:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        time.sleep(2)