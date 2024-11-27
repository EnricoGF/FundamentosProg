def conjCollatz(num):
    if num == 1:
        print("Número Inválido!")
    while num > 1:
        calculo = 0

        if num % 2 == 0: #par
            calculo = num // 2
            print(f"{num} é par: {num} / 2 = {num//2}")
            
        else: #ímpar
            calculo = (num*3) +1
            print(f"{num} é ímpar: {num} * 3 + 1 = {(num*3) +1}")
        num = calculo
        

if __name__ == '__main__':
    n = int(input("Insira um número: "))
    conjCollatz(n)