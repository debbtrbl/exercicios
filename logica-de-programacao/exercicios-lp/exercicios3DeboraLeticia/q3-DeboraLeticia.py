a = float(input("Digite o código: "))
b = float(input("Quantos kg? "))

match a:
    case 1:
        if b <= 5:
            print(f"R$ {(7.00*b):.2f}")
        else:
            print(f"R$ {(5.80*b):.2f}")

    case 2:
        if b <= 5:
            print(f"R$ {(11.80*b):.2f}")
        else:
            print(f"R$ {(8.50*b):.2f}")

    case 3:
        if b <= 5:
            print(f"R$ {(2.25*b):.2f}")
        else:
            print(f"R$ {(1.70*b):.2f}")

    case 4:
        if b <= 5:
            print(f"R$ {(5.50*b):.2f}")
        else:
            print(f"R$ {(4.00*b):.2f}")

    case 5:
        if b <= 5:
            print(f"R$ {(6.90*b):.2f}")
        else:
            print(f"R$ {(5.50*b):.2f}")

    case 6:
        if b <= 5:
            print(f"R$ {(4.50*b):.2f}")
        else:
            print(f"R$ {(2.40*b):.2f}")
