if __name__ == '__main__':
    array = [ 0, 0, 0, 0, 0, 0 ]
    cont = 0

    for x in range(0, 6):
        cont += 2
        array.pop()
        array.insert(x, cont)

    for x in array:
        print(x)