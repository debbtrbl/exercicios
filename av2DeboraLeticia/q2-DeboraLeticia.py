entrada = input().split()
valor = []

for i in entrada:
    valor.append(int(i))

n1 = valor.count(1)
n2 = valor.count(2)
n3 = valor.count(3)
n4 = valor.count(4)
n5 = valor.count(5)
n6 = valor.count(6)

print(f"Número 1 saiu {n1} vezes.")
print(f"Número 2 saiu {n2} vezes.")
print(f"Número 3 saiu {n3} vezes.")
print(f"Número 4 saiu {n4} vezes.")
print(f"Número 5 saiu {n5} vezes.")
print(f"Número 6 saiu {n6} vezes.")

