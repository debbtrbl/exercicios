a = int(input(""))
b = int(input(""))

if a > b:
    x = (a % b)
    
elif b > a:
    x = (b % a)

if x == 0:
    print("Sim")

else:
    print("Não")
