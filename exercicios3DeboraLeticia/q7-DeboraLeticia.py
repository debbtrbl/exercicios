num = int(input("Digite um número: "))

fator = 1

while num > 1:
    fator = num * fator
    num = num - 1
print(fator)
