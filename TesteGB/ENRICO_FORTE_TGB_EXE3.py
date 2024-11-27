import datetime
horario = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

with open('diario.txt', 'a+') as arquivo:
    arquivo.write(f"{horario} - {input('Como você está se sentindo hoje?: ')}")
    arquivo.write('\n')