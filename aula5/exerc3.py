numeros = []

print("Digite números positivos. Digite 0 para encerrar.")
    
while True:
    numero = int(input("Digite um número: "))
        
    if numero == 0:
        break
    elif numero > 0:
        numeros.append(numero)
    else:
        print("Por favor, digite apenas números positivos.")

    if len(numeros) == 0:
        print("Nenhum número positivo foi digitado.")
        

quantidade = len(numeros)
quantidade_pares = sum(1 for n in numeros if n % 2 == 0)
quantidade_impares = quantidade - quantidade_pares
soma = sum(numeros)
media = soma / quantidade
maior = max(numeros)
menor = min(numeros)

print(f"Quantidade de números digitados: {quantidade}")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")