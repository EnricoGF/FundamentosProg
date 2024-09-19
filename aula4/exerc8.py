import math

x1 = float(input("Insira um numero: "))
y1 = float(input("Insira um numero: "))
x2 = float(input("Insira um numero: "))
y2 = float(input("Insira um numero: "))

print(f"A distância entre os pontos P1({x1:.2f}, {y1:.2f}) e P2({x2:.2f}, {y2:.2f}) é: {math.sqrt(((x2-x1)**2)+((y2-y1)**2))}")