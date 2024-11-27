if __name__ == '__main__':
    array = []
    i = 0
    
    while i < 10:
        array.append(int(input("Insira números inteiros e positivos: ")))
        i += 1

    for x in range(len(array)):
        array.insert(len(array)-x, array[x])

    while len(array) > 10:
        array.pop(0)

    for x in range(len(array)):
        print(array[x])