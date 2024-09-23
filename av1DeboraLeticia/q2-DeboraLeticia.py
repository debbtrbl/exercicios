numInicial = int(input(""))
numFinal = int(input(""))
soma = 0

while numInicial < numFinal:
    for i in range(numInicial, numFinal + 1):
        soma = soma + i
    break
print(soma)
    
