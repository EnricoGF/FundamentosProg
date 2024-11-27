if __name__ == '__main__':
    array = [ 12, 45, 84, 2, 28, 35, 35, 67, 21, 2]
    index = ""

    numUser = int(input("Insira um numero: "))

    for x in range(len(array)):
        if array[x] == numUser:
            if index != "":
                index += f", {x}"
            else:
                index += f"{x}"

    if index != "": 
        print(f"{numUser} ENCONTRADO NA(S) POSIÇÃO(ÕES) {index}")

    else:
        print(f"{numUser} NÃO ENCONTRADO")