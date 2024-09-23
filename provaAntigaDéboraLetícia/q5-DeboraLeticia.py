idade = int(input(""))

if idade <= 2:
    print(idade*21)
elif idade > 2 and idade < 5:
    idade = idade - 2
    print(idade*5 + 42)
elif idade > 4 and idade < 8:
    idade = idade - 4
    print(idade*3 + 52)
elif idade > 7:
    idade = idade - 7
    print(idade*2 + 61)
