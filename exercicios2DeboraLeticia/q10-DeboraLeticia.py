a = int(input(""))
b = int(input(""))
op = int(input(""))

match op:
    case 1:
        print(f"{(a**b):.1f}")

    case 2:
        print(f"{((a**2)+(b**2)):.1f}")

    case 3:
        print(f"{(a**(1/2))+(b**(1/2)):.1f}")

    case _:
        print("ERRO")


