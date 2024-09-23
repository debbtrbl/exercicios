produto = float(input("Preço do produto: "))
cod = int(input("Código: "))

match cod:
    case 1:
        print(f"1x de R$ {(produto - (produto*30/100)):.2f}")
    case 2:
        print(f"2x de R$ {(produto - (produto*20/100))/2:.2f}")
    case 3:
        print(f"3x de R$ {(produto - (produto*10/100))/3:.2f}")
    case 4:
        print(f"1x de R$ {(produto/4):.2f}")
    case _:
        print("ERRO")
