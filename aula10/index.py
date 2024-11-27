#Arrays
array = [ 0, 1, 2, 3, 4, 5 ]
tamanho = len(array)
primeiro = array[ 0 ]
ultimo = array[ -1 ] # array[len(array)-1]

arrayMult = [ "a" ] * 5 # printa 5 vezes "a"
sequencia = list(range(0, 10, 1)) # intervalo de 0 a 10 e incrementa 1
listComp = [ x * 2 for x in range(0, 10) ] # x * 2 para cada x dentro do intervalo de 0 a 10

for x in array: # for of
    print(x)

for x in range(len(array)):
    print(x)

array.append(6) # adiciona um elemento no final da array
array.remove("2") # remove o item "2"
array.pop(3) # remove o elemento de uma posição específica
array.clear() # remove todos elementos da array
array.insert(2, 98) # insere na posicao 2 "98"
array.extend(sequencia) # adiciona uma array em outra