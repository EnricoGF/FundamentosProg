preco = float(input("Insira o valor do seu calçado: "))
percDesconto = int(input("Insira o percentual de desconto: "))

descontoMultiplicacao = percDesconto/100

precoDesconto = preco * descontoMultiplicacao #Valor total com desconto
valorDesconto = preco - precoDesconto #Valor descontado do preço total

print("Valor do desconto: {}, Valor total com desconto:{}".format(valorDesconto, precoDesconto))