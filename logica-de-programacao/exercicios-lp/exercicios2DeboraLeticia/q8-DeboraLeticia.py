nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2)/2

if media <= 3.0:
    print(f"{media} - Reprovado")

elif 3.0 < media < 7.0:
    print(f"{media} - Exame")

elif media > 7.0:
    print(f"{media} - Aprovado")
