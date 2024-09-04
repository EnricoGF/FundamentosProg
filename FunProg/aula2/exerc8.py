ativPrat = float(input("Digite sua nota da atividade prática: "))
ativTeor = float(input("Digite sua nota da atividade teórica: "))
provaLab = float(input("Digite sua nota da prova em laboratório: "))
testeTeor = float(input("Digite sua nota do teste teórico: "))
trabExtra = float(input("Digite sua nota do trabalho extraclasse: "))

grauA = (ativPrat * 0.45) + (ativTeor * 0.55)
grauB = (provaLab * 0.6) + (testeTeor * 0.2) + (trabExtra * 0.2)

notaFinal = (grauA * 0.33) + (grauB * 0.67)

print("Sua nota final desta disciplina é: {}".format(notaFinal))