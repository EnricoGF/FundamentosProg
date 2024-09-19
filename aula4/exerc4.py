num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))
num3 = float(input("Insira outro número: "))

if num2 < num1 < num3:
    print("O número digitado está dentro do intervalo.")
elif num2 < num1 > num3:
    print("O número digitado está acima do intervalo.")
elif num2 > num1 < num3:
    print("O número digitado está abaixo do intervalo.")