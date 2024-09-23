venceu = 0

for i in range(6):
    a = str(input(""))
    if a == "v":
        venceu = venceu + 1

if venceu >= 5:
    print("Grupo 1")

elif venceu < 5 and venceu >= 3:
    print("Grupo 2")

elif venceu < 3 and venceu > 0:
    print("Grupo 3")

elif venceu == 0:
    print("-1")
