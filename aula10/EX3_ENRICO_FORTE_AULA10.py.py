if __name__ == '__main__':
    array = []
    i = 0
    
    while i < 10:
        array.append(float(input("Insira números frácionarios: ")))
        i += 1

    maior = max(array)
    menor = min(array)

    for x in range(len(array)):
        if array[x] == maior:
            indexMaior = x
        elif array[x] == menor:
            indexMenor = x

    print(f"a) Maior número:\n\tÍndice: {indexMaior};\n\tNúmero: {maior}")
    print(f"b) Menor número:\n\tÍndice: {indexMenor};\n\tNúmero: {menor}")