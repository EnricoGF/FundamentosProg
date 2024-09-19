vel = input("Insira um valor para velocidade: ")
temp = input("Insira um valor para tempo: ")
dist = input("Insira um valor para distância: ")


if vel == "":
    temp = float(temp)
    dist = float(dist)

    print(f"A velocidade é de {dist / temp} m/s")

elif temp == "":
    vel = float(vel)
    dist = float(dist)

    print(f"O tempo é de {dist / vel} segundos")

elif dist == "":
    vel = float(vel)
    temp = float(temp)

    print(f"A distância é de {vel * temp} metros")
    
else:
    print("Erro!")