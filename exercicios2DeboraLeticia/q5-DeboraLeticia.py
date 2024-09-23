a = int(input(""))
b = int(input(""))
c = int(input(""))

maiorAB = (a+b+abs(a-b))/2
maiorABC = (maiorAB+c+abs(maiorAB-c))/2

if maiorAB == a:
    print(f"{a} é o maior")

elif maiorAB == b and maiorABC == b:
    print(f"{b} é o maior")

elif maiorABC == c:
    print(f"{c} é o maior")
