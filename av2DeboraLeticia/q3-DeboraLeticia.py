entrada1 = input().split()
entrada2 = input().split()

matriz = []
filial = []
repetidos = []

for i in entrada1:
    matriz.append(int(i))

for e in entrada2:
    filial.append(int(e))

for e in matriz:
    if e in filial:
        repetidos.append(e)

for i in range(len(repetidos)):
    print(repetidos[i], end=" ")

