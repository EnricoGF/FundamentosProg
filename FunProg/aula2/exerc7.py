notaTrabalho = float(input("Digite sua nota do trabalho: "))
notaProva = float(input("Digite sua nota da prova: "))
notaTeste = float(input("Digite sua nota do teste: "))

notaFinal = (notaTrabalho * 0.1) + (notaProva * 0.6) + (notaTeste * 0.3)

print("Sua nota final é: {}".format(notaFinal))