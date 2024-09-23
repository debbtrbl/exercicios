cod = int(input(""))
salario = float(input(""))

match cod:
    case 1:
        cargo = "Escrituário"
        aumento = salario*50/100
    case 2:
        cargo = "Secretário"
        aumento = salario*35/100
    case 3:
        cargo = "Caixa"
        aumento = salario*20/100
    case 4:
        cargo = "Gerente"
        aumento = salario*10/100
    case 5:
        cargo = "Diretor"
        aumento = 0
if aumento > 0:       
    novoSalario = salario + aumento
else:
    novoSalario = salario
    
print(cargo)
if aumento > 0:
    print(f"{aumento:.2f}")
else:
    print("Não tem aumento")

print(f"{novoSalario:.2f}")

          
