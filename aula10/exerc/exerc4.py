if __name__ == '__main__':
    array = []
    i = 0
    
    while i < 10:
        array.append(int(input("Insira números inteiros e positivos: ")))
        i += 1

    for x in range(len(array)+1):
        if x != 0:
            print(array[-x])