def media(n1, n2, a):
    if a == "A":
        res = (n1 + n2) / 2
        return res
    elif a == "P":
        res = ((n1*8) + (n2*2)) / 10
        return res

entrada = input().split()
n1 = float(entrada[0])
n2 = float(entrada[1])
a = entrada[2]

print(f"{media(n1, n2, a):.1f}")
