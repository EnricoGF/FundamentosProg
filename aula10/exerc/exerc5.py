if __name__ == '__main__':
    array1 = []
    array2 = []
    i = 0
    
    while i < 10:
        array1.append(int(input("Insira números inteiros e positivos: ")))
        i += 1

    for x in range(len(array1)+1):
        if x != 0:
            array2.append(array1[-x])

    for x in range(len(array1)):
        print("Array original\tArray invertida")
        print("\t",array1[x], "\t\t", array2[x])