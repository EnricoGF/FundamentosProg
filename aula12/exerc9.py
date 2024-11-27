def strToFloat(stringUser):
    if stringUser.replace('.', '', 1).isdigit() and stringUser.count('.') <= 1:
        return float(stringUser)
    else:
        return 0

if __name__ == "__main__":
    texto = input("Digite uma string: ")

    resultado = strToFloat(texto)
    print(f"O valor fracionário correspondente é: {resultado}")