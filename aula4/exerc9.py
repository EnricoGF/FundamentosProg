h = input("Insira a altura (em metros): ")
sexo = input("Insira o sexo (M/F): ")
pesoIdeal = 0

if sexo == "M":
    pesoIdeal = (72.7 * h) - 58
elif sexo == "F":
    pesoIdeal = (62.1 * h) - 44.7

peso = input("Insira o peso: ")

if peso == pesoIdeal:
    print("A pessoa está dentro do peso ideal.")
else:
    print("A pessoa está fora da faixa do peso ideal.")