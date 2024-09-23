atual = float(input(""))
venda = int(input(""))

if venda < 500 or atual < 30:
    novoValor = atual + atual*10/100
elif venda >= 500 and venda < 1200 or atual >= 30 and atual < 80:
    novoValor = atual + atual*15/100
elif venda >= 1200 or atual >= 80:
    novoValor = atual - atual*20/100

print(f"{novoValor:.2f}")
