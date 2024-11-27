def strToInt(stringUser):
    if stringUser.isdigit():  # Verifica se a string é composta apenas por dígitos
        return int(stringUser)
    else:
        return 0

if __name__ == "__main__":
    texto = input("Digite uma string: ")

    resultado = strToInt(texto)
    print(f"O valor inteiro correspondente é: {resultado}")