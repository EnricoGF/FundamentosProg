if __name__ == "__main__":
    frase = input("Insira uma frase: ")
    print(frase.upper())
    print(frase.lower())
    print(frase[0])

    split = frase.split(" ")
    for palavra in split:
        print(palavra[0].upper())