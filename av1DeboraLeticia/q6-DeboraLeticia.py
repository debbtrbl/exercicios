m = int(input(""))
a = int(input(""))
b = int(input(""))

while 40 <= m <= 110 and 1 <= a < m and 1 <= b < m and a != b:
    outro = m - (a + b)
    break
if outro > a and outro > b:
    print(outro)
elif a > outro and a > b:
    print(a)
elif b > a and b > outro:
    print(b)

