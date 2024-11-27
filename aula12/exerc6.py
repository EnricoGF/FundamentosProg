def countOccur(palavraUser):
    ocorrencias = {}
    for caractere in palavraUser:
        if caractere in ocorrencias:
            ocorrencias[caractere] += 1
        else:
            ocorrencias[caractere] = 1
    for caractere, quantidade in ocorrencias.items():
        print(f"'{caractere}': {quantidade}")

if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    
    countOccur(palavra)