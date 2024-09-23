a = float(input("Preço da mercadoria: "))
b = float(input("Desconto: "))
y = a-(a*b/100)
x = a-y
print(f"R$ {x:.2f}")
print(f"R$ {y:.2f}")
