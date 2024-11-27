def avaliarTexto(texto):
    if texto.isdigit():
        print(f"'{texto}' é um número inteiro.")
    elif texto.replace('.', '', 1).isdigit() and texto.count('.') == 1:
        print(f"'{texto}' é um número fracionário.")
    else:
        print(f"'{texto}' é um texto qualquer.")

if __name__ == "__main__":
    textoUser = input("Digite um texto: ")
    
    avaliarTexto(textoUser)