import math

A= int(input("Digite um numero inteiro: "))
B = int(input("Digite um numero inteiro: "))
C = int(input("Digite um numero inteiro: "))
D = int(input("Digite um numero inteiro: "))
E = int(input("Digite um numero inteiro: "))

areaTriangulo = (B * C)/2
perimetroRetangulo = A + B + C + D
areaCirculo = math.pi * E ** 2

print("Área do triângulo: {}".format(areaTriangulo))
print("Perimetro do retângulo: {}".format(perimetroRetangulo))
print("Área do círculo: {}".format(areaCirculo))