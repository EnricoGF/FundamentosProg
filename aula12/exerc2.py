def main(p1, p2):
    if p1 == p2:
        print("As duas palavras são iguais.")
    elif p1 < p2:
        print(f"A palavra '{p1}' é menor que a palavra '{p2}'")
    else:
        print(f"A palavra '{p2}' é menor que a palavra '{p1}'")

if __name__ == "__main__":
    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite outra palavra: ")
    main(palavra1, palavra2)