saldo = float(input(""))

if saldo > 400:
    credito = (saldo*30/100)
elif saldo < 400 and saldo >= 300:
    credito = (saldo*25/100)
elif saldo < 300 and saldo >= 200:
    credito = saldo*20/100
elif saldo < 200:
    credito = saldo*10/100
    
print(f"R$ {credito:.2f}")
