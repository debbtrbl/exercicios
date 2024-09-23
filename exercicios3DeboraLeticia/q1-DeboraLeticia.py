saldo = float(input("Saldo médio: "))

if saldo > 400:
    print(f"R$ {(saldo*30/100):.2f}")

elif saldo <= 400 and saldo > 300:
    print(f"R$ {(saldo*25/100):.2f}")

elif saldo <= 300 and saldo > 200:
    print(f"R$ {(saldo*25/100):.2f}")

if saldo < 200:
    print(f"R$ {(saldo*10/100):.2f}")
