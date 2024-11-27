def palindromo(s):
    return s == s[::-1]

if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    
    if palindromo(palavra):
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")