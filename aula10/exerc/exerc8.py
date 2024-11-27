if __name__ == '__main__':
    array = []

    numUser = int(input("Insira quantos alunos há na turma: "))

    while len(array) < numUser:
        array.append(float(input("Insira a nota final do aluno: ")))

    menorNota = min(array)
    maiorNota = max(array)

    #####################
    
    mediaTurma = 0

    for x in array:
        mediaTurma += x

    mediaTurma /= numUser

    ####################

    vezesMenor = 0
    vezesMaior = 0

    for x in array:
        if x == menorNota:
            vezesMenor += 1
        elif x == maiorNota:
            vezesMaior += 1

    print(f"Resultado da avaliação da turma:\n\nMenor nota: {menorNota} ({vezesMenor})\nMaior nota: {maiorNota} ({vezesMaior})\nMédia da turma: {mediaTurma:.2f}\n\nHistograma das notas:")

    ####################

    cont03 = ""
    cont34 = ""
    cont45 = ""
    cont56 = ""
    cont67 = ""
    cont78 = ""
    cont89 = ""
    cont90 = ""

    for x in range(len(array)):
        x = array[x]
        if 0 <= x <= 3:
            cont03 += "*"
        elif 3.1 <= x <= 4:
            cont34 += "*"
        elif 4.1 <= x <= 5:
            cont45 += "*"
        elif 5.1 <= x <= 6:
            cont56 += "*"
        elif 6.1 <= x <= 7:
            cont67 += "*"
        elif 7.1 <= x <= 8:
            cont78 += "*"
        elif 8.1 <= x <= 9:
            cont89 += "*"
        elif 9.1 <= x <= 10:
            cont90 += "*"

    
    print(f"0.0 ~ 3.0 : {cont03}")
    print(f"3.1 ~ 4.0 : {cont34}")
    print(f"4.1 ~ 5.0 : {cont45}")
    print(f"5.1 ~ 6.0 : {cont56}")
    print(f"6.1 ~ 7.0 : {cont67}")
    print(f"7.1 ~ 8.0 : {cont78}")
    print(f"8.1 ~ 9.0 : {cont89}")
    print(f"9.1 ~ 10.0 : {cont90}")