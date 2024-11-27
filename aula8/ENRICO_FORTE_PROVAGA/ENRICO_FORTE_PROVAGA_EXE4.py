def somar_inversa(num):
    string = "O resultado da soma de "
    soma = 0
    for i in range(1, num+1):
        soma += 1/i
        string += f"1/{i}, "
    string += f"é {soma}"
    return string

if __name__ == '__main__':
    n = int(input("Insira um numero positivo: "))
    print(somar_inversa(n))
