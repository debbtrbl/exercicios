salario = float(input("Sálario: "))
aumento1 = 20
aumento2 = 15

if salario <= 1212.00:
    print(f"R$ {salario + (salario*aumento1/100):.2f}")

else:
    print(f"R$ {salario + (salario*aumento2/100):.2f}")
