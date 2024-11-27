def main(array):
    arraySemDuplicacao = []
    for elem in array:
        if array.count(elem) == 1:
            arraySemDuplicacao.append(elem)

    print(arraySemDuplicacao)

if __name__ == '__main__':
    arrayComDuplicacao = [2, 5, 7, -10, 8, 2, -1, -8, -10, 7, 8, 9, 10]
    main(arrayComDuplicacao)