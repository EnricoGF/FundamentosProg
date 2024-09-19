temp = float(input("Insira uma temperatura em graus Celsius: "))

if temp >= 100:
    print("A água está em estado gasoso.")
elif 0 < temp < 100:
    print("A água está em estado líquido.")
elif temp <= 0:
    print("A água está em estado sólido.")