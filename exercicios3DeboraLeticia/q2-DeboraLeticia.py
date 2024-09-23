custo = float(input("Custo de fábrica: "))

if custo < 35000:
    print(f"R$ {(custo*5/100) + (custo):.2f}")

if custo <= 70000:
    print(f"R$ {(custo + ((custo*10/100)+(custo*15/100))):.2f}")

if custo > 70000:
    print(f"R$ {(custo + ((custo*15/100)+(custo*20/100))):.2f}")
