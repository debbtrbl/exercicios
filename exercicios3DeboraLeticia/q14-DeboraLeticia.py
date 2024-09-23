m = int(input(""))
n = int(input(""))

soma = 0

while n > m:
    for i in range(m,n+1):
        soma = soma+i
    print(soma)
    soma = 0
    m = int(input(""))
    n = int(input(""))


