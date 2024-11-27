def somaTres(quant):
    string= ""
    soma = 0
    for i in range(0,quant):
        string += "3"
        string = int(string)

        soma += string

        string = str(string)
        soma = int(soma)

    print(f"A soma da sequência de números compostos por 3, indo até {quant} dígitos é: {soma}")

if __name__ == '__main__':
    num = int(input("Insira um numero positivo: "))

    somaTres(num)