a = int(input())
s = int(input())
d = int(input())

subida = 0
dias = 0

while subida < a:
    dias = dias + 1 
    subida = subida + s 
    if subida >= a:
        break 
    subida = subida - d 

print(dias)
