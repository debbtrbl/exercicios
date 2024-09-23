num = int(input(""))
soma = 0

while num > 0:
    if num % 3 == 0:
        soma = soma + num
    num = int(input(""))
print(soma)
