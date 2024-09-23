r = int(input(""))
m = int(input(""))
l = int(input(""))

while 1 <= r <= 1000 and 1 <= m <= 1000 and 1 <= l <= 1000:
    if r < m:
        print("RM")
    else:
        print("*")
    if r < l:
        print("RO")
    else:
        print("*")
    break
